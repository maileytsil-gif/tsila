import re
def num(s):
    m = re.search(r'-?\d+(?:[\.,]\d+)?', str(s)); return float(m.group(0).replace(',', '.')) if m else None
def disp_num(p, v):
    s = p.str_for_value(v).strip(); n = num(s)
    if n is not None and ('kHz' in s or 'KHz' in s): n *= 1000.0
    return n
def solve(p, cible):
    lo, hi = p.min, p.max
    croissant = disp_num(p, p.max) > disp_num(p, p.min)
    for _ in range(50):
        mid = (lo + hi) / 2.0
        if (disp_num(p, mid) < cible) == croissant: lo = mid
        else: hi = mid
    p.value = (lo + hi) / 2.0
    return p.str_for_value(p.value).strip()
def set_enum(p, label):
    labels = {}
    for i in range(401):
        v = p.min + (p.max - p.min) * i / 400.0
        labels.setdefault(p.str_for_value(v).strip(), v)
    if label in labels:
        p.value = labels[label]; return label
    return 'NON TROUVE %s (dispo: %s)' % (label, sorted(labels))
