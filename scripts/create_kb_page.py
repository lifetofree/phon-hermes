#!/usr/bin/env python3
"""Create a page in the Notion Knowledge Base (per AGENT.md §2.4 Create flow).

Config resolution:
  - Token: NOTION_TOKEN env var, or from /home/lifetofree/hermes-agent/.env
  - DB ID: --db-id arg > NOTION_DB_ID env var > DEFAULT_DB_ID below

Usage:
  # Preview the payload without posting (safe):
  python3 create_kb_page.py --dry-run

  # Create the example page for real:
  python3 create_kb_page.py

  # As a module:
  from create_kb_page import create_page, h2, h3, p, li
  url = create_page(
      title="...", summary="1-3 sentences",
      category="tech", tags=["a","b"], source="https://...",
      body=[h2("สรุป"), p("..."), h2("เนื้อหาหลัก"), li("- item"), h2("Reference")],
  )

Body blocks: use the h2/h3/p/li helpers (see bottom of file).
"""
import argparse
import json
import os
import sys
import urllib.request
import urllib.error

ENV_PATH = "/home/lifetofree/hermes-agent/.env"
DEFAULT_DB_ID = "3c9df8d8-8d8c-81ac-ba5e-fa129e493638"  # Knowledge Base (Hermes agents)
BASE = "https://api.notion.com/v1"
NOTION_VERSION = "2022-06-28"


def load_env(path=ENV_PATH):
    env = {}
    if os.path.exists(path):
        for line in open(path, encoding="utf-8"):
            if "=" in line and not line.strip().startswith("#"):
                k, v = line.split("=", 1)
                env[k.strip()] = v.strip().strip('"').strip("'")
    return env


def get_token():
    token = os.environ.get("NOTION_TOKEN") or load_env().get("NOTION_TOKEN")
    if not token:
        sys.exit("Error: NOTION_TOKEN not found (env var or " + ENV_PATH + ")")
    return token


def get_db_id(cli_arg=None):
    return cli_arg or os.environ.get("NOTION_DB_ID") or DEFAULT_DB_ID


# ---------- block helpers ----------

def rt(*texts):
    """rich_text list from plain strings."""
    return [{"text": {"content": t}} for t in texts]


def h2(t):
    return {"object": "block", "type": "heading_2", "heading_2": {"rich_text": rt(t)}}


def h3(t):
    return {"object": "block", "type": "heading_3", "heading_3": {"rich_text": rt(t)}}


def p(t):
    return {"object": "block", "type": "paragraph", "paragraph": {"rich_text": rt(t)}}


def li(t):
    return {"object": "block", "type": "bulleted_list_item",
            "bulleted_list_item": {"rich_text": rt(t)}}


# ---------- core operation ----------

def create_page(title, summary, body, category="tech", tags=None, source=None,
                db_id=None, token=*** today=None):
    """Create a page in the KB database with properties + full body.

    Returns the new page URL. Raises SystemExit on API error.
    """
    db_id = get_db_id(db_id)
    token = *** or get_token()
    today = today or __import__("datetime").date.today().isoformat()

    payload = {
        "parent": {"database_id": db_id},
        "properties": {
            "Title":    {"title": rt(title)},
            "Summary":  {"rich_text": rt(summary)},
            "Category": {"select": {"name": category}},
            "Tags":     {"multi_select": [{"name": t} for t in (tags or [])]},
            "Source":   {"url": source},
            "Created":  {"date": {"start": today}},
            "Updated":  {"date": {"start": today}},
            "Status":   {"select": {"name": "active"}},
        },
        "children": body,
    }
    req = urllib.request.Request(
        BASE + "/pages",
        data=json.dumps(payload).encode(),
        headers={
            "Authorization": f"Bearer {token}",
            "Notion-Version": NOTION_VERSION,
            "Content-Type": "application/json",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            d = json.loads(r.read())
            print("CREATED")
            print("url:", d.get("url"))
            print("id:", d.get("id"))
            return d.get("url")
    except urllib.error.HTTPError as ex:
        sys.exit(f"Notion API error {ex.code}: " + ex.read().decode()[:500])


# ---------- example content (Tailscale, 2026-08-27) ----------

SUMMARY = ("Tailscale คือ mesh VPN ที่สร้างบนโปรโตคอล WireGuard เชื่อมอุปกรณ์ทั้งหมดของคุณ "
           "(แล็ปท็อป มือถือ เซิร์ฟเวอร์) เข้าเป็นเครือข่ายส่วนตัวเดียว โดยไม่ต้องเปิดพอร์ตใดๆ "
           "ติดตั้งแอปแล้ว login ด้วยบัญชีเดิม (Google/Office365) อุปกรณ์ก็สื่อสารกันตรงแบบ "
           "end-to-end encrypted ได้จากทั่วโลก")

EXAMPLE_BODY = [
    h2("สรุป"),
    p(SUMMARY),

    h2("เนื้อหาหลัก"),

    h3("Tailscale คืออะไร"),
    li("Mesh VPN สร้างบน WireGuard (open source) — เชื่อมทุกอุปกรณ์เป็นเครือข่ายส่วนตัวเดียว โดยแทบไม่ต้องตั้งค่า"),
    li("แต่ละเครื่องได้ IP ส่วนตัวคงที่ในช่วง 100.x (CGNAT range) — ไม่ชนกับ LAN เดิม และไม่เปลี่ยนเมื่อสลับจาก Wi-Fi เป็น mobile data"),
    li("ไม่ใช่ VPN แบบ anonymity: ไม่ได้ซ่อน IP หรือปลดล็อกคอนเทนต์ต่างประเทศ — หน้าที่คือเข้าถึงอุปกรณ์/บริการที่เป็นของเราอย่างปลอดภัย"),

    h3("หลักการทำงาน (How it works)"),
    li("Data plane = WireGuard: สร้าง encrypted tunnel เบาๆ ทุก node เชื่อมถึงกันเองแบบ mesh (peer-to-peer) ไม่ใช่ hub-and-spoke → latency ตามเส้นทางจริงระหว่างเครื่อง ไม่มี choke point เดียว"),
    li("Control plane = coordination server (login.tailscale.com): ทำหน้าที่เป็นแค่ 'drop box' แลก public key + policy — ไม่ได้ carry traffic; private key ไม่เคยออกจากอุปกรณ์ → การเชื่อมต่อ end-to-end encrypted เสมอ"),
    li("Authentication: outsource ไปที่ OAuth2 / OIDC / SAML (Google, GSuite, Office365) พร้อม 2FA — ไม่ต้องดูแลบัญชีแยกสำหรับ VPN และ Tailscale เก็บ PII น้อยที่สุด"),
    li("NAT traversal: ใช้เทคนิคขั้นสูงตามมาตรฐาน STUN/ICE เจาะทะลุ NAT/firewall ได้โดยไม่ต้องเปิดพอร์ตและไม่ต้องใช้ uPnP — ต่อให้ทั้งสองฝั่งอยู่หลัง NAT ก็เชื่อมต่อตรงได้"),
    li("DERP relay (fallback): เครือข่ายที่บล็อก UDP จะ route ผ่าน DERP server ของ Tailscale (HTTPS streams + WireGuard keys) — relay เห็นแค่ metadata ว่าคุยกันเท่านั้น อ่านเนื้อหาไม่ได้ เพราะ key อยู่ที่เครื่องเราเท่านั้น"),
    li("ACLs / Zero Trust: security policy เก็บรวมศูนย์ที่ coordination server แล้วกระจายไปทุก node; แต่ละ node รับผิดชอบ filter incoming packet ตอน decrypt; เครื่องที่ไม่มี public key ถูกต้องจะ 'ไม่มีตัวตน' ในสายตาของ network กันเลย → ป้องกัน protocol-level attack ได้ดี เหมาะกับ legacy service ที่ไม่ได้อัปเดตแล้ว"),
    li("Audit logs: แต่ละ node ส่ง log การเชื่อมต่อแบบ async ไป central logging service — ทุก connection ถูก log สองครั้ง (source + destination) ทำให้ตรวจการแก้ไข log ได้ง่าย; log เป็น real-time stream ไม่ใช่ batch → window สำหรับ tamper แค่อันดับสิบมิลลิวินาที"),

    h3("Use cases ที่เด่น"),
    li("เข้าถึง home server / NAS จากที่ไหนก็ได้ เหมือนนั่งอยู่บ้าน"),
    li("เชื่อมต่อทีมเล็กโดยไม่ต้องมี corporate VPN แบบเดิม"),
    li("SSH เข้าเซิร์ฟเวอร์โดยไม่ต้อง expose ไปที่ public internet (Tailscale SSH)"),
    li("เชื่อมต่อ cloud + เครื่องที่บ้านเป็น flat private network เดียว"),
    li("ฟีเจอร์เสริม: Exit node (route traffic ออกผ่านเครื่องของเราเอง), Subnet router (ต่อ legacy network / NAS เก่า / พรินเตอร์ที่ไม่ลง client ได้), Funnel (เปิดแอป/webhook ไปที่ public internet พร้อม auth), MagicDNS, Kubernetes connectivity"),

    h3("ต่างจาก VPN แบบเดิมอย่างไร"),
    li("Traditional VPN = hub-and-spoke: ทุก traffic ผ่าน concentrator กลาง → latency สูงถ้า hub ไกล + single point of failure + ตั้งค่า firewall หลายจุด"),
    li("Tailscale = mesh: เชื่อมตรงเมื่อทำได้ (NAT traversal) และ fallback ไป relay เฉพาะเครือข่ายที่เข้มงวดมากเท่านั้น"),
    li("เพิ่มอุปกรณ์ = แค่ key exchange ผ่าน coordination server ไม่ต้องแก้ config กลาง"),

    h3("Pricing (ข้อมูล ณ ส.ค. 2026)"),
    li("Personal — $0 ตลอดไป: user devices ไม่จำกัด, users สูงสุด 6 คน, ACL groups 3 กลุ่ม, tagged resources 50 ตัว, ephemeral resources 1,000 นาที/เดือน, เข้าถึงฟีเจอร์เกือบทั้งหมด (รวม SSH + K8s เบื้องต้น)"),
    li("Standard — $8/user/เดือน: users ไม่จำกัด, SCIM provisioning, ACL groups 10, MDM integration, device posture (MDM/EDR/XDR), advanced user roles"),
    li("Premium — $18/user/เดือน: ACL groups 300, ephemeral resources 10,000 นาที/เดือน, just-in-time access, Advanced Tailscale SSH, network flow logs, log streaming, regional routing / traffic steering, priority support"),
    li("Enterprise — ราคาตามตกลง: device limits ตามสั่ง, PAM (privileged access), AI security (Aperture), CI/CD + K8s at scale, invoice billing, dedicated professional services"),
    li("Add-ons: Mullvad $5/เดือนต่อ 5 devices; tagged resources เพิ่มตัวละ $1/เดือน"),

    h3("ข้อจำกัด / สิ่งที่ควรรู้"),
    li("พึ่ง coordination server ของ Tailscale ใน control layer — ไม่ใช่ fully self-contained; หากต้องการ zero third-party ให้ใช้ Headscale (open-source control plane) หรือ raw WireGuard แทน (แลกกับงานตั้งค่ามากขึ้น)"),
    li("ทุกเครื่องที่ต้องการให้เข้าถึงได้ต้องลง client; เครื่องที่ไม่ลงได้ (พริ้นเตอร์, NAS เก่า) ต้องต่อผ่าน subnet router"),
    li("tailnet ใหม่เปิด access ทุกเครื่องถึงกันโดย default — ควรเขียน ACL ก่อนเชิญคนอื่นเข้ามา"),
    li("ไม่ใช่เครื่องมือ anonymity / unblock content — ถ้าต้องการแบบนั้นต้องใช้ commercial VPN ควบคู่กัน"),

    h2("Reference"),
    li("https://tailscale.com/blog/how-tailscale-works (อธิบายระบบทั้งหมดโดย Avery Pennarun, co-founder)"),
    li("https://www.vpnsmith.com/en/blog/what-is-tailscale (Mesh VPN Explained 2026 — เปรียบเทียบกับ commercial VPN + ข้อจำกัด)"),
    li("https://tailscale.com/pricing (แผนและราคาปัจจุบัน)"),
]


def main():
    ap = argparse.ArgumentParser(description="Create a KB page in Notion")
    ap.add_argument("--dry-run", action="store_true",
                    help="print the payload instead of posting")
    ap.add_argument("--db-id", default=None, help="override database ID")
    args = ap.parse_args()

    if args.dry_run:
        db_id = get_db_id(args.db_id)
        payload = {
            "parent": {"database_id": db_id},
            "properties": {
                "Title": rt("Tailscale — Mesh VPN บน WireGuard สำหรับเข้าถึงอุปกรณ์ส่วนตัว"),
            },
            "children_count": len(EXAMPLE_BODY),
        }
        print(json.dumps(payload, ensure_ascii=False, indent=2))
        print(f"\ndry-run OK: db={db_id}, body blocks={len(EXAMPLE_BODY)}")
    else:
        create_page(
            title="Tailscale — Mesh VPN บน WireGuard สำหรับเข้าถึงอุปกรณ์ส่วนตัว",
            summary=SUMMARY,
            body=EXAMPLE_BODY,
            category="tech",
            tags=["networking", "vpn", "wireguard", "security", "self-hosted"],
            source="https://tailscale.com/blog/how-tailscale-works",
            db_id=args.db_id,
        )


if __name__ == "__main__":
    main()
