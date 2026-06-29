# Case Study: Medical Record Portability Failure — Physical Infrastructure Lock-in

> The third application case of the Anti-Sovereign Design v4 framework.
> Plain-language mappings follow the [glossary](./docs/glossary.md).
> Where E-7 illustrated "territorial sovereignty" and the platform case illustrated "non-territorial sovereignty,"
> this case directly confronts **un-forkable physical infrastructure**.

## 1. Why This Case

Medicine directly governs survival conditions. Life, pain, function, drug access — in
other cases these were "economic survival" or "digital survival," but in medicine,
**physical survival itself** is at stake.

This case tests the framework hard: even if hospital records can be transferred,
hospital buildings, specialists, equipment, and emergency networks cannot be
copied. The 3-layer data portability (data take-away) and the limits of physical
infrastructure forking are exposed simultaneously. In the platform case, "digital
fork is the principle," but here the framework is actually tested on whether it
must apply different principles by sector.

### Core Question

**It is not the patient who chooses the hospital. How much do the hospital,
insurer, record system, and regional infrastructure narrow the patient's options?**

## 2. Applying the Discriminant

### Item 1: Cannot Exit — High

Structural factors that prevent a patient from leaving a hospital:

| What is locked | Description | Substitutability |
| --- | --- | --- |
| Medical records | Test results, surgical history, medication records, allergy information | Low (if records don't transfer, re-testing at the new hospital) |
| Insurance linkage | Private indemnity insurance, health-insurance-approved hospital limits | Medium (depends on the insurer's hospital network) |
| Attending physician relationship | A doctor who knows the patient's condition long-term | Very low (trust and knowledge cannot be transferred) |
| Chronic disease management system | Dialysis, chemotherapy, rehab schedules | Very low (schedule, equipment, staffing dependency) |
| Rare disease centers | Institutions specializing in that disease | None (only a few exist nationwide) |
| Appointment wait | Specialist appointments with waits of months | Low (the wait itself is an exit barrier) |
| Prescription (solution) continuity | Regular prescriptions, narcotic analgesics, specialty drugs | Low (prescription disruption = symptom deterioration) |

Why "cannot exit" is high: the exit cost is not mere inconvenience but leads to
**health deterioration, re-testing costs, and treatment disruption.**

### Item 2: Subjected to Rules — High

Structures in which rules are unilaterally imposed:

- **Internal hospital procedures**: referral letters, appointment rules, test
  sequencing, discharge criteria — no patient choice
- **Insurance review**: health insurance and indemnity insurance coverage/non-
  coverage determinations, review periods — even if the patient objects, the
  insurer decides
- **Referral system**: rules for moving from primary to secondary to tertiary
  hospitals — patients cannot skip levels even if they want to (in principle)
- **Platformed appointment booking**: external booking platforms monopolize
  hospital appointments — changes to platform terms affect hospital access
- **Hospital policy changes**: department reductions, outpatient clinic closures,
  emergency room restrictions — unilateral notice, no patient consent

### Item 3: Redress Doesn't Work — High

Why the formality of complaint procedures is especially severe in medicine:

| Problem | Description |
| --- | --- |
| Information asymmetry | Patients lack the ability to assess the legitimacy of medical judgments |
| Expertise barrier | Without specialized knowledge, patients cannot even raise a dispute |
| Medical dispute cost | Litigation and expert-assessment costs are excessive for the patient, and time-consuming |
| Insurer discretion | The insurer decides the outcome of insurance-review objections — no independence |
| Hospital internal committee | Medical-accident review is conducted by an internal hospital committee — reviewer = adjudicator |
| No redress possible in emergencies | Protest is impossible during emergency treatment |

The crux: in medicine, patients lack the **capacity** to raise a protest at all.
Information asymmetry is more fundamental here than in other cases (E-7's
language barrier, the platform's automated responses).

### Item 4: Holds Survival Conditions — Very High

In medicine, "holding survival conditions" is not metaphor but **literal**:

- **Life**: emergency treatment, treatment of severe disease, surgery
- **Pain**: access to analgesics and anesthesia, chronic pain management
- **Function**: rehabilitation, physical therapy, assistive devices
- **Drugs**: regular prescriptions, specialty drugs, narcotic analgesics
- **Information**: access to one's own test results, diagnoses, treatment plans
- **Time**: wait time itself leads to health deterioration

### Lock-in Severity: Very High

All four items rate high to very high, and the fourth (holds survival
conditions) connects literally to life. In the platform case it was "economic
survival," in E-7 it was "residence and employment," but in medicine
**physical survival itself** is at stake.

## 3. The 3-Layer Data Portability — The Reality in Medicine

Applying the framework's 3-layer data portability to medicine makes each layer's
fulfillment state plainly visible.

### Layer 1: Technical Portability — Partially Met

| Item | Current State |
| --- | --- |
| Medical record issuance | Available on request (legal right) |
| Test results | Must be requested individually per test, not integrated |
| Imaging data (X-ray, MRI) | Available on CD/DVD but format is non-standard |
| Prescription records | Tied to the pharmacy system, not portable |
| Surgical records | Surgical records exist but patient access is limited |

Technically the files can come out, but formats are non-standard and not
integrated. A state of "you can get it, but you can't read it."

### Layer 2: Semantic Portability — Not Met

| Item | Current State |
| --- | --- |
| Medical record format | Each hospital uses a different EMR system, non-standard terminology |
| Test result interpretation | Numbers are given but interpretation must be obtained again |
| Imaging data compatibility | Incompatible with other hospitals' equipment |
| Drug codes | Each hospital uses different drug classification codes |
| Diagnosis codes | ICD codes exist but internal hospital classifications differ |

Even if records are obtained, if the new hospital cannot understand their
meaning, re-testing is necessary. Without semantic portability, technical
portability is meaningless.

### Layer 3: Institutional Portability — Virtually Absent

| Item | Current State |
| --- | --- |
| Test result recognition | New hospital does not accept prior tests and demands re-testing |
| Prescription recognition | New hospital restarts or changes prescriptions |
| Surgical history recognition | New hospital reluctant to take over post-operative care |
| Insurance linkage | Insurance review restarts on hospital change |
| Referral system | Referral letter reissued even with records from another hospital |

Without institutional portability, even if layers 1 and 2 are met, the patient
must undergo re-testing, re-diagnosis, and re-prescription. This is the triple
burden of time, cost, and health deterioration.

### Without Layer 3, "Record Transfer" Is Window Dressing

The absence of the 3-layer data portability is most dramatic in medicine. Even
if a patient carries their medical record to a new hospital:

1. The new hospital does not read the record (semantic portability absent)
2. Even if read, it is not accepted (institutional portability absent)
3. Re-testing follows — the patient endures time, cost, radiation exposure, and pain again

This is not "record transfer" — it is **coerced re-testing**. Without layer 3,
layer 1 is window dressing.

## 4. Physical Infrastructure Lock-in

The core of the medical case is that no matter how much data portability is
secured, **physical infrastructure cannot be copied.** This is where the
framework's "sector-specific fork principle" is actually tested.

### Un-forkable Physical Infrastructure

| Infrastructure | Why It Cannot Be Copied | Lock-in Effect |
| --- | --- | --- |
| Hospital building | Physical structure, location | Number of hospitals in the region = ceiling on choice |
| Specialists | Headcount, training period, licensing | Rare specialists are few nationwide |
| Equipment (MRI, surgical robots) | High cost, installation space, maintenance | Hospitals with the equipment = limited |
| Emergency room | 24-hour staffing and equipment | Regional emergency network = life or death |
| Intensive care unit | Specialized staff, infection control | ICU availability = survival of severe patients |
| Dialysis unit / chemotherapy suite | Regular treatment schedule, equipment | Regular-treatment patients = unable to move |
| Pharmacy / pharmaceutical distribution | Specialty drug distribution network | Rare-drug access = network dependency |

### Regional Medical Monopoly

When a region has only one hospital, or a particular department exists in only one
place:

- **Absence of options**: if there is no other hospital, "choice" does not obtain
- **Emergencies**: if there is only one nearby emergency room, the patient must go
  there even if service quality is low
- **Rare diseases**: centers specializing in a particular disease number only a
  few nationwide
- **Islands and remote areas**: medical access itself is geographic lock-in

Here the core is not fork but **access assurance and limiting monopoly abuse.**
This is the concrete application of the framework's claim that it must apply
different principles by sector:

| Sector | Principle | Application in Medicine |
| --- | --- | --- |
| Digital platform | True fork | (validated in the platform case) |
| Medicine, education, credentials | Portability of recognition | Record transfer + new hospital acceptance → institutional portability |
| Physical infrastructure | Access assurance + monopoly-abuse limitation | Not copying the building but monitoring record transfer, insurance linkage, emergency access, regional monopoly |

The medical case is **the only domain where all three sectors appear
simultaneously.** Records (portability of recognition), equipment and staff
(physical infrastructure), and appointment/telemedicine (digital platform)
overlap. Thus the framework's sector-specific principles are tested not in a
single sector but as a **composite application.**

## 5. Composite Lock-in

Composite lock-in also occurs in medicine. Not the hospital alone, but multiple
systems combine to raise the cost of exit.

### Composite Structure 1: Hospital + Insurer

| Actor | Incentive | Role |
| --- | --- | --- |
| Hospital | Patient retention, revenue | Treatment, testing, prescribing |
| Insurer (health insurance / indemnity) | Cost control, risk management | Coverage/non-coverage determination, review |

Switching hospitals restarts insurance review. Prior tests are not recognized,
and re-testing costs are imposed on the patient. The hospital-insurer linkage
structurally raises the patient's exit cost.

### Composite Structure 2: Hospital + Government Licensing

| Actor | Incentive | Role |
| --- | --- | --- |
| Hospital | License maintenance, licensing | Providing medical services |
| Government (Ministry of Health and Welfare) | Medical quality management, staffing control | Hospital establishment/downsizing approval, specialist assignment |

When the government approves a hospital's downsizing or closure, residents'
medical access is severed. Patients have no part in this decision. The
government-hospital composite determines medical infrastructure, and patients
only bear the consequences.

### Composite Structure 3: Hospital + EMR System

| Actor | Incentive | Role |
| --- | --- | --- |
| Hospital | Holding patient information | EMR operation, record management |
| EMR vendor | Contract retention, data retention | System monopoly, non-standard format |

When EMR systems differ by hospital and the vendor technically obstructs data
movement, patient record transfer is structurally blocked. The EMR vendor's
non-standard format directly undermines data portability layer 2 (semantic
portability).

### Composite Structure 4: Hospital + Pharmacy / Pharmaceutical Distribution

| Actor | Incentive | Role |
| --- | --- | --- |
| Hospital | Prescribing authority | Issuing prescriptions |
| Pharmacy / pharma | Distribution control, inventory management | Supplying specialty drugs |

Specialty drugs, biologics, and narcotic analgesics have limited distribution
networks. Switching hospitals may mean an existing prescription cannot be filled
at a new pharmacy. Prescription continuity depends on the drug distribution
network.

### Composite Structure 5: Hospital + Regional Transportation

| Actor | Incentive | Role |
| --- | --- | --- |
| Hospital | Patient access | Fixed location |
| Regional transit | Route maintenance | Hospital-access transport network |

For patients receiving regular treatment such as dialysis or chemotherapy,
transportation is part of medical access. If the transport network is
disrupted, treatment itself is disrupted. This is the intersection of physical
infrastructure lock-in and regional infrastructure lock-in.

### Lock-in at the Intersection

The same 4-stage pattern seen in E-7 and the platform case repeats:

1. The hospital says "this is continuity of care," the insurer says "this is
   cost management"
2. Re-testing, re-review, and re-prescription arise at the intersection
3. Prescriptions must address hospital, insurer, and pharmacy simultaneously
4. The implementing bodies (Ministry of Health and Welfare, National Health
   Insurance Service) have no reason to reduce their own discretion

## 6. Anti-Sovereign Design Prescriptions

### Prescription Principle: 3-Layer Portability + Physical Infrastructure Access Assurance

In medicine, the 3-layer data portability must be secured simultaneously, while
for physical infrastructure the principle is not fork but access assurance and
limiting monopoly abuse.

### Prescription List

| Prescription | Target | Mechanism | Framework Correspondence |
| --- | --- | --- | --- |
| Standardized medical record portability right | Hospital + EMR vendor | Mandatory standard format, delivery within deadline on patient request | Data portability layers 1+2 |
| Mutual test-result acceptance obligation | Hospital + insurer | Prohibition on refusing another hospital's test results without just cause | Data portability layer 3 |
| Temporary care continuity right for emergency and chronic-disease patients | Hospital + government | Prohibition of treatment/prescription disruption during hospital transition | Injunctive suspension (stop) |
| Minimize prescription and test repetition on hospital change | Hospital | Prohibition of unjustified re-testing; disclosure of reason and cost when re-testing occurs | Exit-cost reduction |
| Compensation for refusal or delay of medical records | Hospital | Compensation obligation for delayed record transfer | Compensation |
| Second-opinion access right for rare and severe disease patients | Hospital + insurer | Subsidy for second-opinion cost, right to change treatment based on second opinion | Objection |
| Regional medical monopoly heatmap disclosure | Kernel (measurement) | Disclosure of hospitals, departments, equipment, and ER availability by region | Lock-in heatmap |
| Pre-impact assessment for hospital closure, relocation, or department reduction | Hospital + government | Patient transfer plan and alternative medical access secured before approval | Injunctive suspension + right of exit |
| Prescription portability assurance | Hospital + pharmacy | Disclosure of reason when a prescription cannot be filled at another pharmacy | Fork feasibility (drugs) |
| Patient direct medical-data access right | Hospital + EMR vendor | Patient API access to and transfer of own data | Data portability layer 1 |

### The Implementing-Body Problem

The same paradox as in E-7 and the platform case:

- **Hospital autonomy**: no reason to voluntarily reduce its own discretion
- **Government regulation**: if the Ministry of Health and Welfare controls
  hospitals, the government is the sovereign. However, since this is a "forced
  right of exit" (record transfer, prohibition of re-testing), it is not
  governance coercion
- **Insurer**: since the National Health Insurance Service is the single insurer,
  changing review criteria is itself governance
- **Direct party rights**: rights the patient exercises independently when
  certain conditions are met — record transfer, refusal of re-testing, and
  second-opinion access

### Mitigation: Applying Forced Right of Exit

The same structure as in the platform case applies to medicine. If the
government tells a hospital "conduct your treatment procedures this way," that
is governance coercion. Instead, the government telling a hospital "you must
ensure the patient can take their records" is a forced right of exit — the power
to open the door, not the power to choose the room.

Regulation must focus not on the hospital's internal treatment policy (governance)
but solely on **exit infrastructure (exit):**
- Mandatory standard format for medical records
- Mandatory mutual acceptance of test results
- Compensation for delayed record transfer
- Patient data API access right

## 7. Lock-in Heatmap

Visualizes how lock-in severity appears differently across situations within the
medical sector:

```
Medical situation      | Exit feasibility (can you leave?) | Rule coercion (are rules strong?) | Redress efficacy (does protest work?) | Dependency asymmetry (can you do without?) | Severity
----------------------|----------|----------|----------|----------|------
Emergency treatment   | Very low | Very high | Very low | Very high | Very high
Chronic disease (dialysis/chemo) | Very low | High | Low | Very high | Very high
Rare disease          | None     | High      | Low      | Very high | Very high
Post-operative care   | Low      | High      | Medium   | High      | High
Routine care (cold, etc.) | High | Low       | Medium   | Low       | Low
Vaccination           | High     | Low       | High     | Low       | Low
Telemedicine (light consultation) | Medium | Medium | Medium | Medium | Medium
```

### Severity Overlap by Patient Type

Even within the same medical system, severity varies by patient type:

```
Patient type          | Emergency treatment | Chronic disease | Post-operative | Routine care
----------------------|----------|--------|--------|---------
Healthy adult        | Medium   | Low    | Low    | Low
Chronic disease patient | Very high | Very high | High | High
Rare disease patient | Very high | Very high | Very high | Very high
Elderly (multi-morbidity) | Very high | Very high | High | High
Pregnant woman        | High     | Medium | Medium | Medium
Child                 | High     | Medium | Medium | Medium
Disabled person       | Very high | High   | High   | High
Regional resident (1 hospital) | Very high | High | High | Medium
```

What this overlap shows: medical lock-in is not a single "hospital-patient"
relationship but is determined at the intersection of **patient health status ×
disease type × regional infrastructure.** Even in the same region, the lock-in
severity of a chronic disease patient and a healthy adult differs extremely.

## 8. Comparing Three Cases — Verifying Framework Universality

Comparing the three cases (E-7, platform, medicine) reveals how each device of
the framework operates in a different context.

### Discriminant Comparison

| Dimension | E-7 visa | Platform account suspension | Medical record transfer |
| --- | --- | --- | --- |
| Sovereignty type | Territorial | Non-territorial | Territorial + physical |
| Survival conditions | Residence, employment | Economic, digital | Life, pain, drugs |
| Cannot exit | High | High | High (plus physical infrastructure) |
| Subjected to rules | High | High | High (plus information asymmetry) |
| Redress doesn't work | Medium–high | High | High (plus expertise barrier) |
| Holds survival conditions | High | High | Very high (life, literally) |
| Composite lock-in | State + employer | Platform + payments/store/ads | Hospital + insurer/government/EMR/pharmacy |

### Verification by Framework Device

| Device | In E-7 | In platform | In medicine |
| --- | --- | --- | --- |
| 3-layer data portability | Very low (institutional absence) | Very low (social graph impossible) | Partial (layer 1 only; layers 2 and 3 absent) |
| Fork feasibility | Limited (other visa types) | Low (network effects) | Impossible (physical infrastructure) |
| Sector-specific fork principle | Not applicable | True fork required | Portability of recognition + access assurance |
| Composite lock-in | 2 actors (state + employer) | 4 structures (platform + payments/store/ads/government) | 5 structures (hospital + insurer/government/EMR/pharmacy/transit) |
| Forced right of exit | Bridge residence period | Forced data portability | Standardized record + mutual acceptance |
| Lock-in heatmap | By visa type | Platform × user type | Medical situation × patient type |

### What the Three Cases Jointly Show

1. **The discriminant applies to all three sovereignty types** — territorial
   (E-7), non-territorial (platform), physical (medicine)
2. **The 4-stage composite lock-in pattern repeats across all three domains** —
   each actor performs only its own role, lock-in arises at the intersection,
   simultaneous prescriptions are needed, and the implementing-body paradox holds
3. **The continuity of lock-in severity is proven** — within the same structure,
   severity varies by user/patient type
4. **The 3-layer data portability is the real bottleneck in every domain** — if
   only layer 1 is met and layers 2 and 3 are absent, portability is window
   dressing
5. **The sector-specific fork principle is genuinely necessary** — digital (true
   fork), medicine (recognition + access), and physical (access assurance only)
   are applied differently

### What the Medical Case Newly Reveals

1. **Physical infrastructure is un-forkable** — even if data is moved, buildings,
   equipment, and staff cannot be copied. The framework's sector-specific
   principle is actually tested
2. **Information asymmetry fundamentally limits redress efficacy** — unlike E-7
   (language) or platform (automation), in medicine the patient lacks the
   capacity to raise a protest at all
3. **Survival conditions are literally life** — qualitatively different from the
   "economic/digital survival" of other cases
4. **Three sectors overlap simultaneously** — medicine is the only domain where
   digital (EMR/appointments), recognition (test results), and physical
   (buildings/equipment) appear at once
5. **The composite lock-in structure is the most complex** — five composite
   structures act simultaneously

## 9. This Case's Impact on the Framework

### What Was Validated

1. **The sector-specific fork principle works** — the three principles of digital
   (fork), medicine (recognition), and physical (access) are applied
   simultaneously within the single domain of medicine
2. **Access assurance works instead of fork for physical infrastructure** — the
   framework does not force fork but applies sector-specific principles, which is
   proven
3. **The 3-layer data portability is most dramatically exposed in medicine** —
   without layer 3, coerced re-testing follows, and the patient bears time, cost,
   and health deterioration
4. **The composite lock-in pattern repeats in a third domain** — the common
   4-stage pattern is proven

### Remaining Challenges

1. **The information-asymmetry problem is unresolved** — patients lack the
   capacity to raise a protest at all. The second-opinion access right is a
   mitigation, but second-opinion cost and accessibility remain a lock-in
2. **Specific mitigations for physical-infrastructure monopoly are not
   established** — when a regional hospital monopoly exists, there are no concrete
   criteria for "access assurance"
3. **Medical staffing shortages are a structural lock-in** — if the number of
   specialists itself is insufficient, changing institutions yields no exit
   option
4. **The meaning of the right of exit in emergencies** — during emergency
   treatment, the "right of exit" does not realistically function. Prior design
   is the only defense

## 10. Next Direction

The three cases have validated the framework's core devices. The next candidate:

- **Family care dependency (care lock-in)** — the domain where the "unable-to-
  exit" is most clearly visible. A lock-in combining economic dependence,
  custody rights, housing, and time. Unlike medicine, "care itself is a
  relationship," so exit means the dissolution of the relationship.
- **Educational credential monopoly (education lock-in)** — a domain entirely
  dependent on institutional portability. A case where technical portability
  exists but is meaningless.
