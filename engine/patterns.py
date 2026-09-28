from __future__ import annotations

def classify_pattern(*, normative=False, functional_requirement=False, harmful=False, frequency=0.0, evidence_of_advantage=False, emerging=False, correlation_known=False):
    if normative or functional_requirement: return "REQUIRED"
    if harmful: return "ANTI_PATTERN"
    if emerging and frequency < .35: return "EXPERIMENTAL"
    if frequency >= .70 and evidence_of_advantage: return "EXPECTED"
    if evidence_of_advantage: return "ADVANTAGE"
    if frequency >= .35: return "TREND"
    if not correlation_known: return "NOT_CORRELATED"
    return "OPTIONAL"
