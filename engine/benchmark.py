from __future__ import annotations
from statistics import median
from typing import Iterable, Dict, List, Optional

def percentile(sorted_values: List[float], p: float) -> Optional[float]:
    if not sorted_values: return None
    if not 0 <= p <= 100: raise ValueError("p must be 0..100")
    xs=sorted(sorted_values)
    if len(xs)==1: return float(xs[0])
    k=(len(xs)-1)*p/100
    f=int(k); c=min(f+1,len(xs)-1); d=k-f
    return round(xs[f]*(1-d)+xs[c]*d,3)

def distribution(values: Iterable[float]) -> Dict[str,float]:
    xs=[float(v) for v in values]
    if not xs: return {}
    return {"n":len(xs),"p25":percentile(xs,25),"p50":percentile(xs,50),"p75":percentile(xs,75),"p90":percentile(xs,90),"p95":percentile(xs,95),"median":round(median(xs),3)}

def frequency(records: Iterable[dict], feature: str) -> Dict[str,float]:
    rs=list(records); n=len(rs)
    count=sum(1 for r in rs if bool(r.get("features",{}).get(feature)))
    return {"observed_count":count,"cohort_size":n,"frequency":round(count/n,4) if n else 0.0}

def classify_sample_size(n:int, mode:str="FULL") -> str:
    minima={"QUICK":12,"FULL":20,"FORENSIC":40,"ELITE":10}
    need=minima.get(mode.upper(),20)
    return "LOW_SAMPLE_SIZE" if n < need else "ADEQUATE"
