from __future__ import annotations
from dataclasses import dataclass
from typing import Dict, Iterable, Optional, Tuple, List

NOT_VERIFIED = "NOT_VERIFIED"

@dataclass(frozen=True)
class ScoreResult:
    score: Optional[float]
    verified_weight: float
    missing: Tuple[str, ...]
    status: str


def weighted_score(values: Dict[str, Optional[float]], weights: Dict[str, float], *, scale_max: float = 10.0, min_verified_weight: float = 0.60) -> ScoreResult:
    """Evidence-aware weighted score.

    Missing dimensions are excluded rather than treated as zero. If verified weight is
    below min_verified_weight, no overall score is emitted.
    """
    unknown = set(values) - set(weights)
    if unknown:
        raise KeyError(f"No weight configured for: {sorted(unknown)}")
    present = {k:v for k,v in values.items() if v is not None}
    missing = tuple(k for k in weights if values.get(k) is None)
    verified_weight = sum(weights[k] for k in present)
    if verified_weight + 1e-12 < min_verified_weight:
        return ScoreResult(None, verified_weight, missing, NOT_VERIFIED)
    for k,v in present.items():
        if not 0 <= float(v) <= scale_max:
            raise ValueError(f"{k}={v} outside 0..{scale_max}")
    numerator = sum(float(present[k])*weights[k] for k in present)
    score = numerator / verified_weight if verified_weight else None
    return ScoreResult(round(score,3) if score is not None else None, round(verified_weight,3), missing, "VERIFIED_PARTIAL" if missing else "VERIFIED")


def awwwards(values: Dict[str, Optional[float]]) -> ScoreResult:
    return weighted_score(values,{"design":.40,"usability":.30,"creativity":.20,"content":.10},min_verified_weight=.70)


def webby(values: Dict[str, Optional[float]]) -> ScoreResult:
    keys=["content","structure_and_navigation","visual_design","functionality","interactivity","innovation","overall_experience"]
    return weighted_score(values,{k:1/7 for k in keys},min_verified_weight=5/7)


def cssda(values: Dict[str, Optional[float]]) -> ScoreResult:
    return weighted_score(values,{"ui":1/3,"ux":1/3,"innovation":1/3},min_verified_weight=2/3)


def fwa(values: Dict[str, Optional[float]]) -> ScoreResult:
    return weighted_score(values,{"concept_strength":.25,"innovation":.20,"craft_execution":.20,"experience_engagement":.15,"technical_execution":.10,"memorability":.10},min_verified_weight=.70)


def digital_excellence(values: Dict[str, Optional[float]], caps: Iterable[float]=()) -> ScoreResult:
    weights={"experience_craft":.25,"ux_usability":.15,"engineering_performance":.20,"seo_discoverability":.15,"accessibility":.10,"content":.05,"conversion":.05,"resilience_security_privacy":.05}
    result=weighted_score(values,weights,scale_max=100,min_verified_weight=.70)
    if result.score is None:
        return result
    final=result.score
    for cap in caps:
        final=min(final,float(cap))
    return ScoreResult(round(final,3),result.verified_weight,result.missing,result.status)
