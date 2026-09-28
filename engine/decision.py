from __future__ import annotations
SEVERITY={"P0":5.0,"P1":4.0,"P2":3.0,"P3":2.0,"P4":1.0}
EFFORT={"very_low":0.75,"low":1.0,"medium":1.5,"high":2.25,"very_high":3.0}

def priority_value(severity:str, impact_breadth:float, confidence:float, leverage:float, effort:str)->float:
    """Ordering helper only; P0..P4 classification remains sovereign."""
    if severity not in SEVERITY or effort not in EFFORT: raise ValueError("Unknown severity/effort")
    if not all(0<=x<=1 for x in [impact_breadth,confidence,leverage]): raise ValueError("0..1 expected")
    return round(SEVERITY[severity]*impact_breadth*confidence*leverage/EFFORT[effort],4)
