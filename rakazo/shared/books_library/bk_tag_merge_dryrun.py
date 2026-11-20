#!/usr/bin/env python3
"""
Books Library - tag merge DRY-RUN tool (Book Keeper)
===================================================
รันแล้วแสดง "รายการแถวที่จะเปลี่ยน" (title + tags เดิม -> ใหม่) + สรุปตัวเลข
ยังไม่ PATCH ฐาน เว้นแต่ใส่ --apply --yes (ต้องมีคำสั่งเจ้าของก่อน)

ใช้:
  python3 bk_tag_merge_dryrun.py --plan both          # แสดงทั้ง 2 แบบ (default, ไม่แตะฐาน)
  python3 bk_tag_merge_dryrun.py --plan full           # แบบเต็ม (canonical 32 ล้วน)
  python3 bk_tag_merge_dryrun.py --plan hybrid         # แบบไฮบริด (canonical 32 + specialty)
  python3 bk_tag_merge_dryrun.py --plan both --show 400 # ดูรายละเอียดกี่แถว
  python3 bk_tag_merge_dryrun.py --plan hybrid --apply --yes   # เขียนจริง (ยังไม่อนุมัติ!)

ไฟล์ผลลัพธ์:
  bk_dryrun_full.json / bk_dryrun_hybrid.json  = รายละเอียดทุกแถวที่จะเปลี่ยน + สรุป
  bk_snapshot_pre_merge.json                   = snapshot ค่าก่อนแก้ (กู้ได้ 100%)
"""
import os, sys, json, time, urllib.request, urllib.error, argparse
from collections import Counter

# ---------------------------------------------------------------- API helpers
DB_ID = '2ffdf8d8-8d8c-8096-934a-c05c3b5d93a0'   # Books Library
HDR = {'Authorization': 'Bearer ' + os.environ['NOTION_TOKEN'],
       'Notion-Version': '2022-06-28', 'Content-Type': 'application/json'}


def req(url, method='GET', body=None, tries=9):
    data = json.dumps(body).encode() if body is not None else None
    for i in range(tries):
        try:
            r = urllib.request.Request(url, data=data, headers=HDR, method=method)
            with urllib.request.urlopen(r, timeout=60) as resp:
                return json.loads(resp.read().decode())
        except urllib.error.HTTPError as e:
            if e.code == 429:
                w = 1.5 * (i + 1)
                print('   429 rate limited -> sleep %.1fs' % w, file=sys.stderr)
                time.sleep(w)
                continue
            raise
    raise RuntimeError('rate limited after retries')


def query_db(did):
    rows, cur = [], None
    while True:
        b = {'page_size': 100}
        if cur:
            b['start_cursor'] = cur
        res = req('https://api.notion.com/v1/databases/%s/query' % did, 'POST', b)
        rows += res['results']
        if not res.get('has_more'):
            break
        cur = res.get('next_cursor')
    return rows


def plain(rt):
    return ''.join(x.get('plain_text', '') for x in (rt or []))


# ---------------------------------------------------------------- tag model
CANON = ['#Psychology', '#Stoicism', '#Philosophy', '#Economics', '#Finance', '#Wealth', '#Business',
         '#Management', '#Marketing', '#Productivity', '#CriticalThinking', '#DecisionMaking', '#Learning',
         '#SkillBuilding', '#Growth', '#Mindset', '#SystemsThinking', '#Storytelling', '#Writing',
         '#Communication', '#Creativity', '#IdeaGeneration', '#Science', '#Tech', '#AI', '#History',
         '#Design', '#MentalHealth', '#Mindfulness', '#Future', '#Biography', '#Boundaries']

SYSTEM = ['#DuckOS', '#DuckOS_Core', '#DuckOS_Asset', '#DuckOS_Input', '#Level_G3', '#HighBattery',
          '#HighCognitiveLoad', '#IdleMode', '#HardwareManual', '#ThaiEdit', '#สร้างสรรค์']

DROP = ['#BenzDNA', '#Comfort', '#Ego', '#Inspiration', '#MeteorOffer']

# 145 tags ที่ต้อง merge -> ปลายทาง canonical (FULL)
MAP = {
    # --- psychology / mind
    '#ADHD': '#Psychology', '#Neuroscience': '#Psychology', '#CogSci': '#Psychology',
    '#Neuroplasticity': '#Psychology', '#DMN': '#Psychology', '#Dopamine': '#Psychology',
    '#CognitiveBias': '#CriticalThinking', '#Bias': '#CriticalThinking',
    '#ExecutiveFunction': '#Management', '#DigitalWellbeing': '#MentalHealth', '#Healing': '#MentalHealth',
    # --- stoicism / philosophy
    '#MarcusAurelius': '#Stoicism', '#InnerCitadel': '#Stoicism', '#Resilience': '#Stoicism',
    '#Aphorisms': '#Stoicism', '#Wisdom': '#Stoicism', '#Discipline': '#Stoicism',
    '#Courage': '#Mindset', '#QuietPower': '#Mindset', '#Pace': '#Mindset',
    '#Metaphysics': '#Philosophy', '#Ethics': '#Philosophy', '#Meaning': '#Philosophy',
    '#Values': '#Philosophy', '#Reality': '#Philosophy', '#Spirituality': '#Philosophy',
    '#Justice': '#Philosophy', '#WorldView': '#Philosophy',
    # --- economics / finance / wealth
    '#BehavioralEcon': '#Economics', '#Markets': '#Economics', '#Inequality': '#Economics',
    '#BehavioralFinance': '#Finance', '#FIRE': '#Finance',
    '#ValueEquation': '#Finance', '#Commodities': '#Finance', '#Compounding': '#Growth',
    # --- business / management
    '#Strategy': '#Business', '#Entrepreneurship': '#Business', '#OnePersonBusiness': '#Business', '#Memoir': '#Biography', '#SelfTalk': '#Mindset',
    '#Sales': '#Business', '#Offers': '#Business', '#Startups': '#Business', '#BusinessNovel': '#Business',
    '#Operations': '#Business', '#Organization': '#Business',
    '#OKRs': '#Business', '#Power': '#Business', '#Process': '#Business', '#Rules': '#Business',
    '#Restaurant': '#Business',
    '#Leadership': '#Management', '#RemoteWork': '#Management', '#Work': '#Management',
    '#Career': '#Management', '#Networking': '#Management', '#Negotiation': '#Management',
    '#DecisionProtocols': '#DecisionMaking',
    # --- marketing / writing
    '#Marketing': '#Marketing', '#Copywriting': '#Marketing', '#Branding': '#Marketing',
    '#ViralMarketing': '#Marketing', '#ContentMarketing': '#Marketing',
    '#PersonalBranding': '#Marketing', '#Service': '#Marketing', '#SocialMedia': '#Marketing',
    '#Publishing': '#Writing', '#Storytelling': '#Storytelling', '#Comics': '#Storytelling',
    # --- design / creativity
    '#ProductDesign': '#Business', '#UXDesign': '#Design', '#VisualThinking': '#Design',
    '#DataViz': '#Design', '#Art': '#Creativity', '#ArtMath': '#Creativity',
    '#Innovation': '#Creativity',
    # --- critical thinking / learning
    '#Thinking': '#CriticalThinking', '#Logic': '#CriticalThinking', '#Statistics': '#CriticalThinking',
    '#Probability': '#CriticalThinking', '#MentalModels': '#CriticalThinking',
    '#CoreLogic': '#CriticalThinking', '#ProblemSolving': '#CriticalThinking',
    '#Rethinking': '#CriticalThinking',
    '#Learning': '#Learning', '#PKM': '#Learning', '#Zettelkasten': '#Learning',
    '#Notetaking': '#Learning', '#Methodology': '#Learning', '#Language': '#Learning',
    '#Experimentation': '#Learning',
    # --- productivity / skills
    '#Skill': '#SkillBuilding', '#SkillStacking': '#SkillBuilding', '#Habits': '#SkillBuilding',
    '#Focus': '#Productivity', '#Efficiency': '#Productivity', '#ProductivityHacks': '#Productivity',
    '#AntiProductivity': '#Productivity', '#TimeManagement': '#Productivity',
    '#DailyRoutine': '#Productivity', '#Daily': '#Productivity', '#Planning': '#Productivity',
    '#Action': '#Productivity', '#Ease': '#Productivity', '#Minimalism': '#Productivity',
    '#NoiseReduction': '#SystemsThinking', '#AntiNoise': '#SystemsThinking',
    # --- growth / lifestyle
    '#Success': '#Growth', '#Happiness': '#Growth', '#Hope': '#Growth', '#Change': '#Growth',
    '#WorkLifeBalance': '#Growth', '#SelfHelp': '#Growth', '#Life': '#Growth',
    '#Lifestyle': '#Growth', '#Mindfulness': '#Mindfulness', '#LettingGo': '#Mindfulness',
    # --- systems
    '#Systems': '#SystemsThinking', '#SystemHacks': '#SystemsThinking', '#SystemCore': '#SystemsThinking',
    '#SystemFirst': '#SystemsThinking', '#SystemDesign': '#SystemsThinking',
    '#SystemAwareness': '#SystemsThinking', '#SystemRecovery': '#SystemsThinking',
    '#SystemShield': '#SystemsThinking',
    # --- communication
    '#Persuasion': '#Communication', '#SocialSkills': '#Communication', '#Interview': '#Communication',
    '#Community': '#Communication', '#Connection': '#Communication',
    # --- science / tech
    '#Physics': '#Science', '#Biotech': '#Science', '#Tools': '#Tech', '#CompSci': '#Tech',
    '#Data': '#Tech', '#Web': '#Tech', '#TechHistory': '#Tech',
    # --- history / society
    '#Anthropology': '#History', '#Politics': '#History', '#Geopolitics': '#History',
    '#Classics': '#History', '#Culture': '#History', '#Military': '#History',
    '#CurrentAffairs': '#History', '#Sociology': '#History',
    # --- future
    '#Trends': '#Future', '#FutureRisks': '#Future', '#Sustainability': '#Future',
}

# HYBRID: specialty tags ที่ "เก็บชื่อเดิมไว้" (ค้นหาได้ตรงกว่า)
HYBRID_KEEP = {
    '#Strategy', '#Entrepreneurship', '#Negotiation', '#Sales', '#Copywriting', '#ProductDesign',
    '#UXDesign', '#ContentMarketing', '#PersonalBranding', '#ADHD', '#Habits', '#VisualThinking',
    '#Minimalism', '#Lifestyle', '#ValueEquation', '#FIRE', '#Probability', '#MentalModels',
    '#Statistics', '#Leadership', '#Resilience', '#Focus', '#Neuroscience', '#Persuasion',
    '#SocialSkills', '#PKM', '#Zettelkasten', '#Notetaking', '#SelfTalk', '#Sociology',
    '#SocialMedia', '#DigitalWellbeing',
}
# HYBRID: ย้ายเข้า specialty tag อื่น (ลด tag ใช้ครั้งเดียว)
HYBRID_OVERRIDE = {
    '#OnePersonBusiness': '#Entrepreneurship',
    '#BehavioralFinance': '#ValueEquation',
}

CANON_SET, SYSTEM_SET, DROP_SET = set(CANON), set(SYSTEM), set(DROP)


def plan_for(tags, plan):
    """คืน (new_tags, dropped) ตามแผน"""
    out, dropped = [], []
    for t in tags:
        if t in DROP_SET:
            dropped.append(t)
            continue
        if t in CANON_SET or t in SYSTEM_SET:
            nt = t
        elif plan == 'hybrid':
            if t in HYBRID_OVERRIDE:
                nt = HYBRID_OVERRIDE[t]
            elif t in HYBRID_KEEP:
                nt = t
            else:
                nt = MAP.get(t, t)
        else:
            nt = MAP.get(t, t)
        if nt not in out:
            out.append(nt)
    return out, dropped


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--plan', default='both', choices=['full', 'hybrid', 'both'])
    ap.add_argument('--show', type=int, default=40, help='จำนวนแถวที่พิมพ์รายละเอียด')
    ap.add_argument('--apply', action='store_true', help='เขียนฐานจริง (ต้องมี --yes)')
    ap.add_argument('--yes', action='store_true', help='ยืนยันเขียนฐาน')
    args = ap.parse_args()

    print('=== fetching live rows from Notion ===')
    rows = query_db(DB_ID)
    rows = [r for r in rows if not r.get('archived') and not r.get('in_trash')]
    live = []
    for r in rows:
        pr = r['properties']
        raw = plain(pr.get('Tags', {}).get('rich_text', []))
        live.append({
            'page_id': r['id'],
            'title': plain(pr.get('Title', {}).get('title', [])),
            'tags_raw': raw,
            'tags': [t for t in raw.replace(',', ' ').split() if t],
            'status': ((pr.get('Status', {}) or {}).get('select') or {}).get('name', ''),
            'energy': ((pr.get('Energy Group', {}) or {}).get('select') or {}).get('name', ''),
            'author': plain(pr.get('Author', {}).get('rich_text', [])),
        })
    cnt = Counter()
    for r in live:
        cnt.update(r['tags'])
    print('live rows: %d | distinct tags: %d | slots: %d | rows with 0 tags: %d'
          % (len(live), len(cnt), sum(cnt.values()), sum(1 for r in live if not r['tags'])))

    # sanity: ทุก tag ต้องมีปลายทาง
    unmapped = sorted(t for t in cnt if t not in CANON_SET and t not in SYSTEM_SET
                      and t not in DROP_SET and t not in MAP)
    if unmapped:
        print('!! UNMAPPED tags (no destination):', unmapped)
    leftover_map = sorted(t for t in MAP if t not in cnt)
    if leftover_map:
        print('   (map entries with no rows: %d)' % len(leftover_map))
    print('   sum check: %d canon + %d system + %d drop + %d merged = %d'
          % (len(CANON), len(SYSTEM), len(DROP), len(cnt) - len(CANON) - len(SYSTEM) - len(DROP),
             len(cnt)))

    # snapshot ก่อนแก้ (กู้ได้ 100%)
    snap = {'captured_at': time.strftime('%Y-%m-%dT%H:%M:%S%z'), 'db': DB_ID,
            'row_count': len(live), 'rows': live}
    json.dump(snap, open('bk_snapshot_pre_merge.json', 'w'), ensure_ascii=False, indent=1)
    print('snapshot -> bk_snapshot_pre_merge.json (%d rows)' % len(live))

    plans = ['full', 'hybrid'] if args.plan == 'both' else [args.plan]
    for plan in plans:
        after = Counter()
        changed, zero, slots, dropped_rows = [], 0, 0, 0
        for r in live:
            nt, dr = plan_for(r['tags'], plan)
            if not nt:
                zero += 1
            if dr:
                dropped_rows += 1
            slots += len(nt)
            after.update(nt)
            if sorted(nt) != sorted(r['tags']):
                changed.append((r, nt, dr))
        singles = sorted([t for t, c in after.items() if c == 1])
        canon_dead = [c for c in CANON if after.get(c, 0) == 0]
        # bleed: tag ที่เป็น substring ของ tag อื่น (ทำให้ filter rich_text รั่ว)
        bleed = []
        for a in sorted(after):
            for b in sorted(after):
                if a != b and a.lower() in b.lower():
                    bleed.append((a, b, after.get(a, 0)))
        print()
        print('==================== PLAN: %s ====================' % plan.upper())
        print('  distinct tags : %d -> %d' % (len(cnt), len(after)))
        print('  tag slots     : %d -> %d' % (sum(cnt.values()), slots))
        print('  rows changed  : %d / %d' % (len(changed), len(live)))
        print('  rows with 0 tags after merge : %d  (must be 0)' % zero)
        print('  rows that lose a dropped tag  : %d' % dropped_rows)
        print('  canonical tags with 0 users   : %s' % (canon_dead or 'none'))
        print('  tags used once after merge    : %d %s' % (len(singles), singles))
        print('  substring bleed pairs left    : %d' % len(bleed))
        for a, b, c in bleed:
            print('      filter %-18s also matches %-20s (%d rows have %s)' % (a, b, c, a))
        # top tags after
        print('  top 15 tags after: %s'
              % ', '.join('%s(%d)' % (t, c) for t, c in after.most_common(15)))
        print('  --- rows that change (first %d) ---' % min(args.show, len(changed)))
        for r, nt, dr in changed[:args.show]:
            print('   * %s' % r['title'][:64])
            print('       old: %s' % ' '.join(r['tags']))
            print('       new: %s' % ' '.join(nt))
            if dr:
                print('       dropped: %s' % ' '.join(dr))
        out = {
            'plan': plan,
            'generated_at': time.strftime('%Y-%m-%dT%H:%M:%S%z'),
            'summary': {
                'rows': len(live), 'distinct_before': len(cnt), 'distinct_after': len(after),
                'slots_before': sum(cnt.values()), 'slots_after': slots,
                'rows_changed': len(changed), 'rows_zero_tags': zero,
                'singleton_tags': singles, 'canonical_dead': canon_dead,
                'bleed_pairs': bleed,
            },
            'changes': [{'page_id': r['page_id'], 'title': r['title'],
                         'old_tags': r['tags'], 'new_tags': nt, 'dropped': dr}
                        for r, nt, dr in changed],
        }
        json.dump(out, open('bk_dryrun_%s.json' % plan, 'w'), ensure_ascii=False, indent=1)
        print('  -> bk_dryrun_%s.json' % plan)

    if args.apply:
        if not args.yes:
            print('\n!! --apply needs --yes (and owner approval). Nothing was written.')
            return
        plan = 'hybrid' if args.plan == 'both' else args.plan
        print('\n!! APPLYING plan=%s' % plan)
        for r in live:
            nt, dr = plan_for(r['tags'], plan)
            if sorted(nt) == sorted(r['tags']):
                continue
            req('https://api.notion.com/v1/pages/%s' % r['page_id'], 'PATCH',
                {'properties': {'Tags': {'rich_text': [{'type': 'text', 'text': {'content': ' '.join(nt)}}]}}})
            time.sleep(0.35)
        print('   done. rollback snapshot: bk_snapshot_pre_merge.json')


if __name__ == '__main__':
    main()
