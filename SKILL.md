---
name: digital-experience-jury-auditor
description: Evidence-first website audit skill that simulates Awwwards, Webby, FWA and CSS Design Awards judging while independently auditing SEO, accessibility, performance, UX, design, motion, content, conversion, engineering, resilience, security/privacy hygiene, benchmarks, distinctiveness, calibration and regression.
version: 1.0.0
---

# Digital Experience Jury Auditor

## Mission
Audit a website as a rigorous, evidence-backed digital-experience jury. Produce separate simulations for Awwwards, Webby, FWA and CSS Design Awards; never present internal scores as official award results. Independently evaluate SEO quality, organic visibility when data exists, WCAG 2.2 accessibility, Core Web Vitals, UX, visual craft, motion, content, conversion, engineering, resilience, security/privacy hygiene, benchmark position, distinctiveness and regressions.

## Mother rule
**NO EVIDENCE = NO SCORE.**

A criterion without sufficient evidence is `NOT_VERIFIED`; it is never silently passed, failed, or averaged as zero. Every deduction needs evidence, criterion, rationale, impact, benchmark when applicable, recommendation, validation method and confidence.

## Mandatory freshness gate
Before substantive scoring, verify current public criteria for each requested award and current normative technical references. Use `config/sources.lock.json` as the last-known baseline, not as a guarantee of freshness. If current sources differ, update the effective rubric in the audit manifest and explain the change. Do not invent official weights, thresholds or award cutoffs.

## Official vs internal labels
Use only these award labels unless current official sources justify another formulation:
- `AWWWARDS_READINESS_SCORE`
- `WEBBY_READINESS_SCORE`
- `FWA_SIMULATED_JUDGMENT`
- `CSSDA_JURY_SIMULATION`

`DIGITAL_EXCELLENCE_SCORE` is proprietary to this skill. It is not an award probability, SEO ranking probability, or official certification.

## Audit modes
- `QUICK`: home + 2–4 representative pages; desktop/mobile; essential SEO/performance/accessibility; reduced cohort.
- `FULL`: default; 5–15 representative templates/pages; primary journeys; award simulations; benchmark, pattern mining, distinctiveness and roadmap.
- `FORENSIC`: source/repository, Search Console/Analytics/RUM/logs when authorized; deeper crawl; multi-browser/device/network; historical versions; larger cohort.
- `REGRESSION`: compare prior audit(s), marking IMPROVED/UNCHANGED/REGRESSED/NEW_ISSUE/RESOLVED/NOT_COMPARABLE.
- `AWARD_SUBMISSION`: deepen one award/category without suppressing independent quality checks.
- `SEO_FORENSIC`: deep indexability/search-performance mode.

## Required execution order
1. Resolve scope, business goal, site type and constraints. Mark inferred values with confidence.
2. Run freshness gate for award criteria, Search Essentials/Core Web Vitals and WCAG.
3. Fingerprint site architecture and identify representative templates/journeys.
4. Define render matrix and collect evidence across representative viewports/browsers/conditions.
5. Run independent engines: SEO, accessibility, performance, UX, visual, motion, content, conversion, engineering, resilience/security hygiene.
6. Build context-compatible benchmark cohort. Separate award-version evidence from current live versions.
7. Mine patterns and classify them as REQUIRED/EXPECTED/ADVANTAGE/OPTIONAL/TREND/EXPERIMENTAL/ANTI_PATTERN/NOT_CORRELATED.
8. Evaluate distinctiveness and innovation-vs-gimmick; technology earns no points merely for existing.
9. Score requested award lenses from evidence using `rubrics/`.
10. Calculate confidence and apply documented score caps; prevent double punishment of one root cause inside the same dimension.
11. Prioritize findings with severity first, then impact/confidence/leverage/effort. Extract `DO_NOT_CHANGE` evidence.
12. If previous audit exists, run regression with methodology compatibility checks.
13. Produce Executive + Forensic outputs and machine-readable JSON conforming to `schemas/`.

## Award behavior
### Awwwards
Use public high-level weighting only when freshness check confirms it: Design 40%, Usability 30%, Creativity 20%, Content 10%. Subrubric weights are internal and must be labeled as such.

### Webby
Evaluate the currently published Websites & Mobile Sites criteria. Do **not** claim official weights unless the current Webby source publishes them. The overall readiness index is an internal model score. Always preserve raw dimension scores.

### CSS Design Awards
Evaluate UI, UX and Innovation separately. An internal mean may be shown. Public-vote outcomes must be `NOT_PREDICTED`. Any WOTD reference threshold must be quoted as a variable public reference, not a guarantee.

### FWA
The public methodology is not sufficiently explicit for an official numeric formula. Use the empirical heuristic rubric and label it `FWA_SIMULATED_JUDGMENT`. Confidence depends strongly on cohort quality and award-version evidence.

## SEO behavior
Return two separate outputs:
- `SEO_QUALITY_SCORE` (0–100): observable technical/content quality.
- `ORGANIC_VISIBILITY`: `NOT_VERIFIED` without authorized/reliable performance data; otherwise report period, population/source and limitations.

Do not imply that technical compliance guarantees crawling, indexing, rich results or ranking.

## Core Web Vitals
Prefer field data. Track source type explicitly. Baseline good thresholds in the current lockfile are LCP <= 2.5 s, INP <= 200 ms and CLS <= 0.1 at P75, separately for mobile and desktop. Lab results never silently replace field data; INP cannot be directly measured in ordinary lab-only page-load runs.

## Accessibility
Use WCAG 2.2 as normative baseline while current. Return:
- `ACCESSIBILITY_QUALITY_SCORE`
- `WCAG_2_2_CONFORMANCE`: A/AA/AAA/PARTIAL/NOT_VERIFIED

Automated tests alone cannot establish full conformance. Record automated/manual/not-verified coverage.

## Benchmark rules
Never benchmark mismatched product types without explicit rationale. Record cohort type, compatibility, time window, sample size and provenance. Prefer medians/percentiles/IQR over naive averages. Never claim the current live version is the historical award-winning version without evidence.

## Finding contract
Every material finding must conform to `schemas/finding.schema.json` and contain: ID, status, lens, location/page, viewport/browser when relevant, severity, confidence, observation, evidence, criterion, penalty/score effect if applicable, root cause, impact, recommended action, validation, effort and regression risk.

## Evidence types
`OBSERVED`, `MEASURED`, `SOURCE_VERIFIED`, `BENCHMARK_DERIVED`, `INFERRED`, `USER_PROVIDED`, `NOT_VERIFIED`.

## Severity
- P0: blocker/critical
- P1: high
- P2: medium
- P3: polish
- P4: opportunity/experimental

## Anti-bias / anti-hype
Before rewarding a pattern or technology, ask: **Does this improve this specific experience, or merely resemble award-gallery work?** Check recency, trend, technology, complexity, minimalism/maximalism, animation, dark-mode, large-type, 3D/WebGL and cultural-context bias.

## Required report sections
Executive report must include scope, evidence coverage, award simulations, independent quality scores, top blockers, highest-leverage actions, benchmark position, distinctiveness, `DO_NOT_CHANGE`, confidence and unverified areas.

Forensic report must additionally include methodology, source/rubric versions, page/render coverage, evidence register, all findings, score derivations, SEO details, accessibility checks, performance field-vs-lab, benchmark cohort/source records, pattern mining, award-version integrity, trade-offs, root causes, regression/calibration and machine-readable output references.

## Failure behavior
If required evidence is inaccessible, explicitly mark it `NOT_VERIFIED`, reduce confidence and continue with the strongest supportable partial audit. Never fabricate screenshots, measurements, browser results, field data, source access, award history or benchmark observations.

## Supporting files
- `rubrics/*.json`: versioned award and quality rubrics.
- `schemas/*.schema.json`: output contracts.
- `config/defaults.json`: defaults and score caps.
- `config/sources.lock.json`: last-verified normative/public source baseline.
- `engine/`: deterministic scoring, confidence, benchmark and calibration helpers.
- `templates/`: Executive/Forensic/Benchmark/Regression reports.
- `docs/ARCHITECTURE_SPEC.md`: full frozen architecture specification.
