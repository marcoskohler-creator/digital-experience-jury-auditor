from pathlib import Path
import json, sys
ROOT=Path(__file__).resolve().parents[1]
required=["SKILL.md","README.md","docs/ARCHITECTURE_SPEC.md","config/defaults.json","config/sources.lock.json","rubrics/awwwards.json","rubrics/webby.json","rubrics/cssda.json","rubrics/fwa.json","schemas/finding.schema.json","templates/executive-report.md","templates/forensic-report.md"]
missing=[p for p in required if not (ROOT/p).exists()]
for p in ROOT.rglob("*.json"):
    json.loads(p.read_text())
if missing:
    print("FAIL missing:",missing); sys.exit(1)
print(f"PASS: {len(required)} required files present; JSON parse OK")
