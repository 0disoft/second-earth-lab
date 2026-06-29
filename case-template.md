# Case Analysis Template

> Template used when applying a new case to the Anti-Sovereign Design v4 framework.
> For plain-language mappings, follow the [terminology mapping table](./docs/glossary.md).
> This template standardizes the structure standardized after five case applications (E-7, platform, healthcare, care, education).
> A complete analysis requires all sections to be filled.

## How to Use

1. Copy this file and rename it to `case-<name>.md`.
2. Fill in each section following its instructions.
3. Replace the bracketed guidance (`[...]`) with actual content.
4. After completion, add it to the document composition table in README.md.

---

## 1. Why This Case

> Describe in one paragraph which aspect of the framework this case tests.
> State which of the five sovereignty types tested across the five cases (territorial, non-territorial, physical, relational, recognition regime)
> it falls under, or whether it constitutes a new sovereignty type.

[Describe why this case tests the framework hard.]

### Core Question

[State the core question this case raises in one sentence.]

### Proposition This Case Tests

[Whether it tests an existing proposition of the framework or proposes a new one.]

## 2. Applying the Discriminant

> Apply the four items of the lock-in discriminant to each actor.
> If two or more actors are locked in, write each separately (care: provider+recipient, education: student+parent+teacher).

### [Actor A — e.g., user, patient, student]

| Dimension | Score (0–5) | Evidence | Confidence |
| --- | ---: | --- | --- |
| Exit infeasibility | | [Structural factors preventing exit] | High / Medium / Low |
| Rule coerciveness | | [Unilateral rule imposition] | High / Medium / Low |
| Redress ineffectiveness | | [Practical efficacy of redress procedures] | High / Medium / Low |
| Dependency asymmetry | | [Specific content of dependency asymmetry] | High / Medium / Low |

### [Actor B — if applicable]

| Dimension | Score (0–5) | Evidence | Confidence |
| --- | ---: | --- | --- |
| Exit infeasibility | | | |
| Rule coerciveness | | | |
| Redress ineffectiveness | | | |
| Dependency asymmetry | | | |

### Persona Scores

> Score at least two personas. Use the weighted severity formula from [lock-in-score.md](./docs/methodology/lock-in-score.md).
> severity = 0.25 × exit_infeasibility + 0.20 × rule_coerciveness + 0.20 × redress_ineffectiveness + 0.35 × dependency_asymmetry

| Persona | Exit infeasibility | Rule coerciveness | Redress ineffectiveness | Dependency asymmetry | Weighted severity | Confidence |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| High-bargaining-power persona | | | | | | |
| Low-bargaining-power persona | | | | | | |
| Transition-state persona | | | | | | |

### Lock-in severity: [Score] (Actor A), [Score] (Actor B)

> If dependency asymmetry scores 4 or above, lock-in severity is high even if the other three dimensions are moderate.

[Describe the reasoning for the severity assessment.]

## 3. Data Portability (Taking Your Data With You) — Three Layers

> Assess technical (Layer 1), semantic (Layer 2), and institutional (Layer 3) portability separately.
> Identify which layer is the bottleneck in this case.

### Layer 1: Technical Portability — [Met/Partial/Absent]

| Item | Current Status |
| --- | --- |
| [Data type 1] | [Whether exit is possible] |
| [Data type 2] | |

### Layer 2: Semantic Portability — [Met/Partial/Absent]

| Item | Current Status |
| --- | --- |
| [Compatibility item 1] | [Whether interpretable by other systems] |
| [Compatibility item 2] | |

### Layer 3: Institutional Portability — [Met/Partial/Absent]

| Item | Current Status |
| --- | --- |
| [Recognition/interoperability item 1] | [Whether other institutions recognize it] |
| [Recognition/interoperability item 2] | |

### Bottleneck Analysis

[Describe which layer, if absent, renders the other layers meaningless.]

## 4. Composite Lock-in

> Identify structures where two or more actors create lock-in through their respective, differing incentives.
> Check whether the four-stage common pattern recurs.

### List of Composite Structures

| # | Actor A (role) | Actor B+ (role) | Intersection lock-in |
| --- | --- | --- | --- |
| 1 | | | |
| 2 | | | |
| 3 | | | |
| ... | | | |

### Four-Stage Pattern Stress Test

1. **Each actor performs only its own role** — [each actor's point of agreement]
2. **Lock-in arises at the intersection** — [what a single-sector audit cannot see]
3. **The prescription must resolve the intersection simultaneously** — [what happens if only one side is resolved]
4. **The implementer's paradox** — [which actor holds the authority to adopt the prescription]

## 5. Relational Lock-in (If Applicable)

> Structures where two or more actors are bound together in different ways.
> If the lock-in is singular (state/platform/healthcare), this section may be omitted.

### Lock-in Structure

- **[Actor A] is bound to [what]**
- **[Actor B] is bound to [what]**
- **[Actor C — if applicable] is bound to [what]**

### Exit Harm

> Check whether one person's exit threatens another's survival.
> Compare with care (exit = neglect) and education (school district change = admission track disruption).

| Exiting actor | Impact on third parties |
| --- | --- |
| | |

## 6. Anti-Sovereign Design Prescriptions

> Present prescriptions for resolving lock-in. For each prescription, indicate which
> mechanism of the framework it corresponds to.

### List of Prescriptions

| # | Prescription | Target | Mechanism | Framework Correspondence |
| --- | --- | --- | --- | --- |
| 1 | | | | [Data portability / enforced right of exit / objection / fork / ...] |
| 2 | | | | |
| 3 | | | | |
| ... | | | | |

### The Implementer Problem

[Describe which actor holds the authority to adopt the prescription, and the paradox
that this actor has no reason to reduce its own authority.]

### Sector-Specific Fork Principles

| Sector | Core Principle | Application in This Case |
| --- | --- | --- |
| [Relevant sector] | [Real fork / recognition portability / access guarantee / alternative care / recognition pluralism] | |

## 7. Lock-in Heatmap

> Visualize lock-in severity across internal variations (user types, tracks, stages)
> in this case.

### [Classification axis 1] × [Classification axis 2]

```
[Type A]     | Exit infeasibility | Rule coerciveness | Redress ineffectiveness | Dependency asymmetry | Severity
[Type B]     |           |           |           |           |
[Type C]     |           |           |           |           |
```

### Anomalies

[Describe paradoxes or exceptional patterns revealed by the heatmap.
e.g., homeschooling paradox — exit feasibility is high, but absence of recognition makes dependency asymmetry very high]

## 8. Comparison with Existing Cases

> Compare this case with existing cases (E-7, platform, healthcare, care, education).

### Discriminant Comparison

| Dimension | E-7 | Platform | Healthcare | Care | Education | [This case] |
| --- | --- | --- | --- | --- | --- | --- |
| Sovereignty type | Territorial | Non-territorial | Physical | Relational | Recognition regime | |
| Survival conditions | | | | | | |
| Number locked in | 1 | 1 | 1 | 2+ | 3 | |
| Third-party impact on exit | None | None | None | Survival threat | Track disruption | |
| Redress capacity | | | | | | |

### Form of the Right of Exit

| Case | Form of right of exit | Core demand |
| --- | --- | --- |
| [This case] | | |

## 9. This Case's Impact on the Framework

### What Was Tested

1. [Whether existing propositions of the framework hold in this case]
2. ...

### Newly Revealed

1. [New dimensions or concepts not present in the existing framework]
2. ...

### Promotion Candidates

> If any concept newly discovered in this case merits promotion to framework.md,
> state it explicitly. Promotion criterion: whether it is a universal concept that can be retroactively applied to existing cases.

| Concept | Promoted? | Promotion location (candidate) |
| --- | --- | --- |
| | [Promoted/Held] | |

### Remaining Tasks

1. [Problems unresolved in this case]
2. ...

## 10. Conclusion — Contribution to Framework Transferability

[Describe in one paragraph how this case extends/tests/challenges the
transferability of the framework.]
