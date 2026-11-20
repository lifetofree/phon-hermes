#!/usr/bin/env python3
import json, importlib.util, sys

live = json.load(open('bk_verify_post_merge.json'))
opts = set(live['tag_options'])

spec = importlib.util.spec_from_file_location('m', 'bk_tag_merge_dryrun.py')
m = importlib.util.module_from_spec(spec)
sys.argv = ['x', '--plan', 'hybrid']
spec.loader.exec_module(m)

canon = set(m.CANON)
sysm = set(m.SYSTEM)
keep = set(m.HYBRID_KEEP)
ov = m.HYBRID_OVERRIDE
expected = canon | sysm | set(ov.values()) | keep

print('expected(plan) size :', len(expected))
print('live options        :', len(opts))
print('in live not expected:', sorted(opts - expected))
print('in expected not live:', sorted(expected - opts))
