# Source Refresh Protocol

Run before every substantive audit when current award/SEO/accessibility policy matters.

1. Check each requested award's official current judging/criteria page.
2. Record access timestamp and exact source URL.
3. Compare public dimensions/weights/thresholds with `config/sources.lock.json`.
4. If different, do not silently overwrite history: record an effective audit rubric version and change note.
5. Verify Google Core Web Vitals current metrics/thresholds and field/lab guidance.
6. Verify current W3C accessibility recommendation baseline.
7. Mark inaccessible or ambiguous methodology explicitly; downgrade confidence instead of inventing rules.
8. Use official sources first; secondary commentary may inform context but cannot define an 'official' formula.
