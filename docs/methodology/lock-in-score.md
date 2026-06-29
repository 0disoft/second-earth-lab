# Lock-in Severity Score — Measurement Model

> Companion to [framework.md](../../framework.md) Section 5.
> This document makes the scoring model explicit so that independent analysts
> can reproduce severity scores and challenge them.

## 1. Purpose

The lock-in severity score is not a verdict. It is a structured estimate
that forces the analyst to decompose a lock-in claim into four dimensions
and assign a defensible weight to each. The score is only as good as the
evidence behind it; low-evidence scores must be marked as such.

## 2. Score Range

0.0 – 5.0

| Range | Label | Interpretation |
| --- | --- | --- |
| 0.0 – 0.9 | Negligible | Exit is realistic; discomfort, not lock-in |
| 1.0 – 1.9 | Low | Exit is possible but costly |
| 2.0 – 2.9 | Moderate | Exit requires significant sacrifice |
| 3.0 – 3.9 | High | Exit is nearly impossible without external help |
| 4.0 – 5.0 | Severe | Exit is structurally blocked; survival conditions held by another |

## 3. Dimensions and Weights

| Dimension | Weight | Question |
| --- | --- | --- |
| Exit infeasibility | 0.25 | Can the person leave without losing survival conditions? |
| Rule coerciveness | 0.20 | Are the imposed rules non-negotiable and externally enforced? |
| Redress ineffectiveness | 0.20 | Does challenge produce change? |
| Dependency asymmetry | 0.35 | Does another actor hold the person's survival conditions? |

```
severity = 0.25 * exit_infeasibility
         + 0.20 * rule_coerciveness
         + 0.20 * redress_ineffectiveness
         + 0.35 * dependency_asymmetry
```

Dependency asymmetry carries the highest weight because the discriminant's
core claim is that lock-in is not merely difficulty but the structural
condition where survival conditions are held by another.

## 4. Per-Dimension Scoring

Each dimension is scored 0–5.

| Score | Meaning |
| --- | --- |
| 0 | No constraint in this dimension |
| 1 | Minor constraint, easily overcome |
| 2 | Moderate constraint, requires effort |
| 3 | Significant constraint, requires major sacrifice |
| 4 | Severe constraint, exit nearly blocked |
| 5 | Total blockage in this dimension |

### Exit infeasibility

| 0 | 1 | 2 | 3 | 4 | 5 |
| --- | --- | --- | --- | --- | --- |
| Free exit, alternatives available | Exit possible, alternatives exist | Exit possible but costly | Exit requires major sacrifice | Exit nearly impossible | Exit structurally blocked |

### Rule coerciveness

| 0 | 1 | 2 | 3 | 4 | 5 |
| --- | --- | --- | --- | --- | --- |
| Rules are voluntary | Rules are customary but unenforced | Rules are enforced but challengeable | Rules are legally binding, limited appeal | Rules are binding, no appeal | Rules are binding, challenge produces retaliation |

### Redress ineffectiveness

| 0 | 1 | 2 | 3 | 4 | 5 |
| --- | --- | --- | --- | --- | --- |
| Challenge works immediately | Challenge works with delay | Challenge partially works | Challenge rarely works | Challenge is purely formal | No challenge mechanism exists |

### Dependency asymmetry

| 0 | 1 | 2 | 3 | 4 | 5 |
| --- | --- | --- | --- | --- | --- |
| Self-sufficient | Mild dependence | Moderate dependence | Heavy dependence on one actor | Survival conditions held by another | Survival conditions held by another, no alternative exists |

## 5. Intervention Threshold

| Severity | Action |
| --- | --- |
| < 2.0 | Monitor; no intervention required |
| 2.0 – 2.9 | Design preventive mechanisms (portability, fork feasibility) |
| 3.0 – 3.9 | Active intervention (injunctive suspension, mandatory portability) |
| ≥ 4.0 | Structural intervention (recognition pluralism, alternative infrastructure, sunset clause) |

## 6. Confidence Level

Each score must carry a confidence label.

| Confidence | Meaning |
| --- | --- |
| High | Based on primary sources (law, regulation, verified data, direct testimony) |
| Medium | Based on secondary sources or indirect evidence |
| Low | Based on analytical inference or analogy |

A score with low confidence is not invalid, but it must be flagged so that
readers know where to direct scrutiny.

## 7. Persona Variation

The same structure produces different severity for different people.
Each case study must score at least two personas.

| Persona type | Why it matters |
| --- | --- |
| High-bargaining-power user | Establishes the floor — if this person is locked in, the structure is severe |
| Low-bargaining-power user | Establishes the ceiling — most vulnerable person in the same structure |
| Transition-state person | Someone undergoing job change, illness, or account suspension — captures dynamic severity |

## 8. Worked Example — E-7 Visa Holder (Low Bargaining Power)

| Dimension | Score | Reasoning |
| --- | --- | --- |
| Exit infeasibility | 4 | Cannot leave employer without losing residence permit; bridge stay is short |
| Rule coerciveness | 4 | Immigration law is binding; appeal is formal but rarely succeeds |
| Redress ineffectiveness | 3 | Complaint mechanism exists but employer retaliation is common |
| Dependency asymmetry | 5 | Employer holds both job and residence; no alternative sponsor readily available |

```
severity = 0.25 * 4 + 0.20 * 4 + 0.20 * 3 + 0.35 * 5
         = 1.0 + 0.8 + 0.6 + 1.75
         = 4.15 → Severe
```

Confidence: Medium (based on immigration law and reported cases, not a survey).

## 9. Limitations

- The weights are a starting point, not a claim of optimality. They should be
  challenged with evidence from repeated application.
- The model assumes the four dimensions are commensurable. In practice,
  dependency asymmetry may dominate to a degree that the linear model
  understates.
- Persona scores are not averages. The framework's design principle is to
  design for the worst-positioned person, so the highest persona severity
  is the structure's severity for intervention purposes.
- This model does not capture temporal dynamics — how severity changes during
  war, job loss, illness, or account suspension. A longitudinal extension is
  future work.

## 10. What This Model Does Not Do

- It does not prove lock-in exists. It structures the argument so that others
  can check each dimension and disagree.
- It does not prescribe intervention. It maps severity to a threshold, but
  the choice of intervention remains political.
- It does not replace judgment. A structure scoring 2.9 may be more urgent
  than one scoring 3.1 if the context demands it.
