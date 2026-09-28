from __future__ import annotations

def confidence(evidence_coverage: float, benchmark_fit: float, measurement_quality: float, repeatability: float) -> float:
    vals=[evidence_coverage,benchmark_fit,measurement_quality,repeatability]
    if any(v<0 or v>1 for v in vals):
        raise ValueError("Confidence inputs must be 0..1")
    return round(100*(.35*evidence_coverage + .25*benchmark_fit + .20*measurement_quality + .20*repeatability),1)

def band(score: float) -> str:
    if score >= 90: return "VERY_HIGH"
    if score >= 80: return "HIGH"
    if score >= 60: return "MEDIUM"
    return "LOW"
