from __future__ import annotations
from statistics import median
from typing import Iterable, Dict

def sanity_check(scores: Iterable[float], labels: Iterable[str], *, winner_labels=("winner","elite")) -> Dict:
    pairs=[(float(s),str(l).lower()) for s,l in zip(scores,labels)]
    if not pairs: return {"status":"FAIL","reason":"empty_sample"}
    winners=[s for s,l in pairs if l in winner_labels]
    ordinary=[s for s,l in pairs if l not in winner_labels]
    checks=[]; status="PASS"
    if winners and median(winners)<7.0:
        checks.append({"id":"over_severity","pass":False,"detail":"Median recognized-winner simulation below 7.0."}); status="FAIL"
    else: checks.append({"id":"over_severity","pass":True})
    if ordinary and sum(s>=9 for s in ordinary)/len(ordinary)>.20:
        checks.append({"id":"score_inflation","pass":False,"detail":">20% non-winner fixture scores >=9."}); status="FAIL"
    else: checks.append({"id":"score_inflation","pass":True})
    return {"status":status,"sample_size":len(pairs),"checks":checks,"winner_median":median(winners) if winners else None,"ordinary_median":median(ordinary) if ordinary else None}
