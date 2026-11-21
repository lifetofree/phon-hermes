import numpy as np
from PIL import Image
import sys, hashlib

def blackcols(path):
    im = Image.open(path).convert("RGB")
    a = np.asarray(im)
    h = a.shape[0]
    top = int(h * 0.21)
    bot = int(h * 0.67)
    band = a[top:bot, :, :]
    if band.size == 0:
        return None
    blackfrac = (band.max(axis=2) <= 8).mean(axis=0)   # fraction of pixels that are pure-ish black
    cols = np.where(blackfrac >= 0.5)[0]
    # group into runs
    runs = []
    for c in cols:
        if runs and c == runs[-1][1] + 1:
            runs[-1][1] = c
        else:
            runs.append([int(c), int(c)])
    # edge darkness (mean luminance of outer 40 cols)
    lum = (0.2126*a[:,:,0] + 0.7152*a[:,:,1] + 0.0722*a[:,:,2])
    left = float(lum[:, :40].mean())
    right = float(lum[:, -40:].mean())
    mid = float(lum.mean())
    return dict(size=im.size, md5=hashlib.md5(open(path,'rb').read()).hexdigest(),
                n_black_cols=int(len(cols)), runs=runs[:8], left40=round(left,1),
                right40=round(right,1), mean_lum=round(mid,1))

for p in sys.argv[1:]:
    try:
        print(p, blackcols(p))
    except Exception as e:
        print(p, "ERR", e)
