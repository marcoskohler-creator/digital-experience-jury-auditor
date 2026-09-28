from __future__ import annotations

def compare(previous, current, *, higher_is_better=True, tolerance=1e-9, methodology_compatible=True):
    if not methodology_compatible or previous is None or current is None:
        return {"status":"NOT_COMPARABLE","delta":None}
    delta=float(current)-float(previous)
    if abs(delta)<=tolerance: status="UNCHANGED"
    elif (delta>0)==higher_is_better: status="IMPROVED"
    else: status="REGRESSED"
    return {"status":status,"delta":round(delta,4)}
