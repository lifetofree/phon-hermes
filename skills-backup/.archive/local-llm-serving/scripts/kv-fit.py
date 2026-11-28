#!/usr/bin/env python3
"""Estimate KV cache size for a GGUF model at given context lengths.

Usage: python kv-fit.py <model.gguf> [ctx ...]
       (default ctxs: 32768 65536 131072 262144)

Prints KV GB at f16 / q8_0 / q4_0 per ctx. Compare with
`nvidia-smi` + `free -h`: KV beyond VRAM spills to RAM (works,
slower prefill on long prompts).

Requires the gguf package (this box: ~/llama.cpp/llama-env).
"""
import os
import sys

from gguf import GGUFReader


def val(r, key):
    c = r.fields[key].contents
    if callable(c):
        c = c()
    if isinstance(c, list):
        return c[0]
    return c


def find(r, suffix):
    for k in r.fields.keys():
        if k == suffix or k.endswith('.' + suffix):
            return k
    return None


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    path = sys.argv[1]
    ctxs = [int(x) for x in sys.argv[2:]] or [32768, 65536, 131072, 262144]
    r = GGUFReader(path)
    L = val(r, find(r, 'block_count'))
    kvh = val(r, find(r, 'attention.head_count_kv')) or val(r, find(r, 'attention.head_count'))
    hd = val(r, find(r, 'attention.head_size'))
    if hd is None:
        # same fallback llama.cpp uses when head_size is absent
        hd = val(r, find(r, 'embedding_length')) // val(r, find(r, 'attention.head_count'))
    meta = val(r, find(r, 'context_length'))
    w = os.path.getsize(path) / 1024**3
    print('model: %s  (%.2f GB)' % (os.path.basename(path), w))
    print('layers=%s kv_heads=%s head_dim=%s metadata_ctx=%s' % (L, kvh, hd, meta))
    ept = 2 * L * kvh * hd  # K+V, per token
    print('KV elements/token = %s' % ept)
    for name, b in (('f16', 2.0), ('q8_0', 1.0625), ('q4_0', 0.5625)):
        pt = ept * b
        cells = '  '.join('%dk=%.2fG' % (c // 1024, pt * c / 1024**3) for c in ctxs)
        print('  %-6s %.3f MB/tok   %s' % (name, pt / 1024**2, cells))


if __name__ == '__main__':
    main()
