# Digital Experience Jury Auditor

Production-oriented skill package generated from the frozen 3,031-line architecture specification.

This package separates public award criteria from internal explanatory subrubrics and enforces **No evidence = no score**. It includes deterministic helpers, JSON Schemas, reporting templates, benchmark/calibration scaffolding and unit tests.

## Important
This skill simulates award judging. It does not claim to be Awwwards, Webby, FWA or CSS Design Awards, and it does not produce official scores, certifications or guaranteed award outcomes.

## Quick validation
```bash
python -m unittest discover -s tests -v
python engine/validate_package.py
```

## Primary files
- `SKILL.md` — runtime contract
- `docs/ARCHITECTURE_SPEC.md` — complete design specification
- `docs/METHODOLOGY.md` — implementation methodology
- `config/sources.lock.json` — reference freshness baseline
- `rubrics/` — award/quality models
- `schemas/` — machine-readable contracts
- `engine/` — deterministic helpers
- `templates/` — report output formats
- `benchmarks/` — cohort and calibration scaffolding
