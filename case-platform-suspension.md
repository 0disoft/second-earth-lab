# Case Study: Platform Account Suspension — Sovereignty Without Territory

> The second applied case of the Anti-Sovereign Design v4 framework.
> Plain-language mappings follow the [glossary](./docs/glossary.md).
> Where E-7 demonstrated "state + employer composite lock-in,"
> this case demonstrates **sovereignty without territory**.

## 1. Why This Case

The E-7 case examined territorial sovereignty — the structure in which a state
controls the right to reside within its borders. Platform account suspension
reveals a different kind of sovereignty. There is no territory; instead of
borders there are APIs, instead of civil registration there are accounts, and
instead of deportation there is account suspension.

Why this case matters for the framework: it demonstrates that the lock-in
discriminant is not bound to territorial boundaries and applies equally to a
**non-territorial sovereign**. When the state is disaggregated into territorial
sovereigns, the vacancy left behind is filled by the platform — a structure this
case makes plainly visible.

### The Angle of Inquiry

We do not descend into shallow arguments like "if you violated the terms of
service, suspension is fair." That is not the question. The question is:

**How completely does account suspension sever an individual's social and
economic conditions of survival — and for that disposition, are explanation,
objection, suspension, portability, and compensation available?**

From this angle, it becomes clear why the platform is a modern sovereign.

## 2. Non-Territorial Sovereignty (Power Without Land)

The platform possesses the same sovereign structure as a state, yet has no
territory. This difference must be made explicit.

| State Sovereignty | Platform Sovereignty | Structural Equivalence |
| --- | --- | --- |
| Territory | Platform ecosystem (API, store, protocol) | Same: access-controlled domain |
| Civil registration | Account | Same: unit of identification and tracking |
| Borders | Login / API permissions / store review | Same: entry control |
| Citizenship | Terms-of-service agreement | Same: condition of membership |
| Deportation | Account suspension / ban | Same: forced exit |
| Law | Terms of service / algorithmic policy | Same: rule imposition |
| Judiciary | Customer support / appeal form | Same: redress procedure (large gap in practical power) |
| Taxation | Fees / data collection / ad revenue | Same: resource extraction |

The absence of territory is not a weakness but a **strength**. Territorial
sovereignty is constrained by physical limits to expansion, but platform
sovereignty expands globally through network effects. A single platform's
"citizenry" can outnumber a nation's population.

### The Account Is Identity

In the modern digital environment, a platform account is not merely a service
subscription — it functions as **digital identity**:

- **Authentication**: "Log in with Google," "Log in with Apple" — the key to
  accessing other services
- **Payment**: App store purchases, subscriptions, in-app payments
- **Social graph**: Contacts, messages, followers, reputation
- **Content storage**: Photos, documents, email, cloud storage
- **Business infrastructure**: Ad accounts, developer accounts, seller accounts,
  creator revenue
- **Enterprise work tools**: Email, calendar, collaboration tools, document
  sharing

When a single account is suspended, this entire chain severs. This is not
"losing access to one service" — it is **the revocation of digital citizenship**.

## 3. Applying the Discriminant

### Clause 1: Cannot Exit — High

The scope of what an account binds:

| What Is Bound | Consequence at Suspension | Substitutability |
| --- | --- | --- |
| Email | Communication severed, password recovery for other services impossible | Low (email-based authentication is standard) |
| Social graph | Contacts, followers, reputation vanish | Very low (graph cannot be replicated) |
| Purchase history | Access to apps, movies, music, books lost | None (purchases are platform-internal) |
| Payment method | Subscriptions, in-app payments severed | Medium (alternative payment methods exist) |
| Authentication | Cannot access services dependent on "Log in with Google" | Low (high OAuth dependency) |
| Photos / documents | Cloud storage access lost | Medium (if backed up) |
| Business account | Ad, sales, revenue generation severed | Low (entire business suspended) |

Why "cannot exit" is high: it is not departure from a single service but
**departure from an entire digital ecosystem**. Changing email alone requires
password recovery, contact migration, subscription resets, and
re-authentication — and during this process, access to other services can be
permanently lost.

### Clause 2: Subjected to Rules — High

The unilateral nature of rule imposition:

- **Terms-of-service changes**: Advance notice exists, but there is no effective
  right to refuse. "If you don't agree, you can't use the service" — this is not
  consent; it is coercion.
- **Automated suspension**: Algorithms suspend accounts. Unintended suspensions
  (false positives) can occur at scale.
- **Algorithmic adjudication**: The reason for suspension is automatically
  classified by an algorithm, often without any human judgment involved.
- **Monopoly on terms interpretation**: The platform holds a monopoly on the
  criteria for judging "terms violation." The standard is not legal but the
  platform's internal policy, and that policy is opaque.

### Clause 3: Objection Is Ineffective — High

The formality of redress procedures:

| Problem | Description |
| --- | --- |
| No customer support | No access to live agents; only automated responses repeat |
| Automated appeals | After form submission, an automated algorithm reviews; no human review |
| Insufficient explanation | No specific reason provided beyond "terms violation" |
| Time pressure | Account remains suspended during appeal processing; livelihood disruption continues |
| No discretion | No higher authority to appeal the decision |
| Limits of legal remedy | Small-scale users cannot afford litigation; arbitration clauses mandatory |

Core point: a redress procedure exists, but the entity operating it is the same
entity that issued the disposition. There is no judicial independence. This is
structurally equivalent to a state where "the police prosecute, the police
judge, and the police hear the appeal."

### Clause 4: Holds Survival Conditions — High (Very High Depending on Group)

The degree to which account suspension severs survival conditions varies by
user type:

| User Type | Severity of Survival-Condition Severance | Description |
| --- | --- | --- |
| General user (hobby) | Low | Inconvenient but unrelated to survival |
| General user (auth-dependent) | Medium | Loses access to other services; recovery takes time |
| Freelancer / creator | High | Revenue channel severed; fanbase access lost |
| Business / seller | Very high | Revenue severed; inventory, employees, contracts cascade |
| Developer (app-store-dependent) | Very high | App distribution channel severed = business shutdown |
| Ad operator | Very high | Ad account suspended = zero revenue |
| Enterprise (work-tool-dependent) | Very high | Email, documents, calendar severed = work paralysis |

It becomes clear here that "holding survival conditions" is a continuous value
depending on user type. For a hobby user it may not constitute lock-in; for a
business it is unambiguous lock-in. This is concrete evidence for why the
framework's lock-in severity score is not a binary judgment.

### Lock-in Severity: High (Very High for Business and Auth-Dependent Groups)

## 4. Composite Lock-in

Composite lock-in appears in platform account suspension as well. It is not a
single platform but the combination of multiple systems that raises the cost of
exit.

### Composite Structure 1: Platform + Payment Network

| Actor | Incentive | Role |
| --- | --- | --- |
| Platform (Google/Apple) | Ecosystem control, fee revenue | Account, app distribution, authentication |
| Payment network (card company / PG) | Transaction processing, risk management | Payment approval, suspension linkage |

When the payment network is linked to platform suspension, the user loses not
only the account but the entire payment infrastructure. Refund disputes,
payment halts, and cascading subscription cancellations occur simultaneously.

### Composite Structure 2: Platform + App Store

| Actor | Incentive | Role |
| --- | --- | --- |
| Platform (OS provider) | Ecosystem control | Monopoly over app distribution channel |
| App store review | Quality control, policy compliance | App approval, rejection, removal |

For a developer, app store account suspension is not a mere "service
suspension" but **the dissolution of an entire business foundation**. When an
app is removed, existing user access is severed, revenue drops to zero, and
investment value evaporates. No alternative marketplace exists (for iOS, the
App Store is the only one).

### Composite Structure 3: Platform + Advertising Market

| Actor | Incentive | Role |
| --- | --- | --- |
| Content platform (YouTube/Meta) | Operating the content ecosystem | Creator account, monetization |
| Ad network (AdSense, etc.) | Ad efficiency, brand safety | Ad delivery, revenue distribution |

For a creator, platform account suspension means simultaneous severance of
audience access and revenue. Even if an alternative platform exists, the social
graph (subscribers) cannot be transferred, making effective exit impossible.

### Composite Structure 4: Platform + Government/Enterprise Identity Authentication

| Actor | Incentive | Role |
| --- | --- | --- |
| Platform | User management | OAuth, SSO, account authentication |
| Government / enterprise | Digital administration, work efficiency | Adopts platform-based authentication |

When government services or enterprise work tools depend on platform
authentication (OAuth), platform account suspension severs access to public
services and work. In this structure, the platform is a private company that
functions as **public infrastructure**.

### Lock-in at the Intersection

The same pattern as E-7 repeats. Each actor performs only its own role:

- Platform: "This is enforcement of service terms"
- Payment network: "This is transaction risk management"
- App store: "This is store policy compliance"
- Government / enterprise: "This is authentication dependency"

But the cost of exit produced by their combination is classified as no single
actor's responsibility. It is cross-sector lock-in invisible to any
single-sector audit.

## 5. Structural Comparison with E-7

| Dimension | E-7 Visa | Platform Account Suspension |
| --- | --- | --- |
| Sovereignty type | Territorial (territory-based) | Non-territorial (network-based) |
| Sovereign | State + employer | Platform + payment/store/ad/government |
| Identification unit | Foreign registration number | Account ID |
| Rule imposition | Immigration law | Terms of service / algorithms |
| Forced exit | Deportation | Account suspension |
| Redress procedure | Administrative appeal / litigation (slow but exists) | Customer support (fast but formalistic) |
| Alternative route | Other visa types (limited) | Other platforms (effectively impossible due to network effects) |
| Data portability | Very low (no institutional portability) | Very low (social graph non-portable) |
| International comparison | Other countries' visa systems exist | Global platforms have no substitutes |

### Commonality: The Coercion Paradox

Both cases share a structure in which the actor with the authority to adopt a
remedy sees its own authority reduced by that remedy. The platform has no reason
to voluntarily curtail its own discretion, and if the state forcibly regulates
the platform, the state becomes the sovereign again.

### Difference: Quality of Redress Procedure

E-7 has a legal framework, albeit slow. The platform's redress procedure is
fast but lacks judicial independence — the reviewer is the same entity as the
one that issued the disposition. This shows that on the "objection is
ineffective" clause, the platform can be more severe than E-7.

### Difference: Existence of Alternatives

E-7 permits limited exit to other visa types or other countries. For platforms,
alternatives effectively do not exist due to network effects. Moving from
YouTube to Twitch means nothing if the audience doesn't follow. This
demonstrates that "fork feasibility" is structurally constrained in digital
platforms.

## 6. Applying Sector-Specific Fork Feasibility

The framework holds that fork principles differ by sector. Applied to platforms:

### Digital Platforms — Fork Feasibility Must Be Highest

The framework demands a "real fork" for digital platforms: portability of data,
social graph, content, payment history, and reputation.

Current state:
- **Data portability**: A "download my data" feature exists, but it satisfies
  only technical portability (layer 1) of the three-layer data portability model.
  Semantic portability (layer 2) and institutional portability (layer 3) are
  absent. Receiving files is meaningless if no other platform can read them.
- **Social graph portability**: Effectively impossible. Contacts can be
  exported, but follower and subscriber relationships are platform-internal.
- **Content portability**: Downloadable, but metadata and interaction records
  (likes, comments) are non-portable.
- **Payment history**: The purchase itself remains on record, but access rights
  to purchased content are non-transferable. Movies, apps, and books must be
  re-purchased on another platform.
- **Reputation portability**: Platform-internal ratings, reviews, and
  verification status are non-portable.

Conclusion: digital platforms currently fail to meet any of the "real fork"
conditions the framework demands. It is the precise embodiment of "you can see
everything but you cannot leave."

### Fork-Cost Asymmetry

Fork costs are imposed only on the user:
- When a user leaves a platform: data reconstruction, social graph rebuilding,
  re-investment in purchases — all borne by the user
- When a platform suspends a user: zero cost — executed instantly

This asymmetry is the core of lock-in. Exit costs exist only for the user;
expulsion costs are nearly zero for the platform.

## 7. Anti-Sovereign Design Prescriptions

### Prescription Principle: Five Rights Must Be Guaranteed

The framework's five requirements — explanation, objection, injunctive
suspension (halt), compensation, and fork feasibility — applied to platform
account suspension.

### Prescription List

| Prescription | Mechanism | Framework Correspondence |
| --- | --- | --- |
| Pre-suspension notice (except emergencies) | Notify reason and evidence 72 hours before suspension; provide opportunity to respond | Explanation |
| Emergency livelihood account temporary restoration right | Accounts tied to livelihood, healthcare, or legal obligations operate temporarily during appeal | Injunctive suspension |
| Third-party appeal body | Appeals heard by an independent body, not internal to the platform | Objection |
| Automated-disposition log disclosure | Disclose algorithmic suspension criteria, thresholds, and false-positive rates | Explanation + right to measure disclosure |
| Data / social graph / purchase history portability | Export in standard format + mandatory acceptance by other platforms | Fork feasibility |
| Separation and protection of business and personal accounts | Prohibit suspending business accounts for personal terms violations | Survival-condition protection |
| Per-platform lock-in heatmap disclosure | Disclose suspension rate, appeal success rate, average restoration time | Constitutionalization of right to measure |
| Affected-group right of rebuttal | Right of counter-audit by creator and business associations | Audit system |
| Compensation for invalid suspension | Mandatory compensation for damages caused by wrongful suspension | Compensation |

### The Enforcement Actor Problem

The same paradox as E-7 repeats:

- **Platform self-regulation**: No reason to voluntarily curtail its own
  discretion
- **State regulation**: The state becomes the sovereign again. However, in this
  case the state performs not "coercion of governance" but "coercion of the
  right of exit," which aligns with the framework's direction. The state's
  authority must be limited solely to lock-in release.
- **Third-party body**: Difficult to secure independence. If budget, selection,
  or authority depends on the platform or government, it becomes subordinate.
- **Direct party rights**: Grant temporary restoration as a legal right. Not
  something the platform "permits," but a right the user can exercise
  unilaterally upon meeting certain conditions.

### Mitigation: Applying Coercion of the Right of Exit

The framework's distinction between "coercion of governance vs. coercion of the
right of exit" operates here.

If the state specifically directs the platform on "how to conduct account
suspension procedures," that is coercion of governance — a new sovereign
setting the rules.

Instead, the state mandating "that users be able to take their data with them"
is coercion of the right of exit — the power to open doors, not the power to
design rooms.

For this distinction to function in practice, regulation must focus not on
platform internal policy (governance) but solely on **exit infrastructure
(exit)**:
- Mandate data portability standards
- Require social graph portability
- Guarantee the independence of third-party appeal bodies
- Mandate compensation for invalid suspension

## 8. Lock-in Heatmap

Visualizing the lock-in structure by platform type:

```
Platform Type        | Exit Feasibility (can you leave?) | Rule Coercion (are rules strong?) | Redress Efficacy (do objections work?) | Dependency Asymmetry (do you need it?) | Severity
---------------------|----------|----------|----------|----------|------
OS ecosystem (Apple)  | Very low | Very high | Low      | Very high | Very high
OS ecosystem (Google) | Low      | High      | Low      | Very high | Very high
Social media          | Medium   | High      | Medium   | High      | High
Content platform      | Medium   | High      | Medium   | High      | High
Email/cloud           | Low      | Medium    | Medium   | High      | High
Payment/advertising   | Low      | High      | Low      | Very high | Very high
Work tools (enterprise) | Low    | Medium    | Medium   | Very high | Very high
Single-purpose service | High   | Low       | Medium   | Low       | Low
```

### What the Heatmap Shows

- OS ecosystems (Apple/Google) carry the highest severity — absence of
  alternatives, authentication dependency, and payment monopoly combined
- Single-purpose services (e.g., weather apps) have low lock-in severity —
  substitutable, unrelated to survival conditions
- Work tools are very high at the enterprise level — the entire workflow depends
  on one platform
- Payment/advertising is very high for businesses — monopoly over revenue
  channels

### Severity Overlap by User Type

Even on the same platform, severity differs by user type:

```
User Type              | OS Ecosystem | Social Media | Payment/Ad | Work Tools
-----------------------|----------|-----------|----------|--------
Hobby user             | Medium   | Low       | Low      | Low
Auth-dependent         | High     | Medium    | Medium   | Medium
Creator                | High     | Very high | Very high| Medium
Business/seller        | Very high| High      | Very high| High
Developer              | Very high| Medium    | High     | Medium
Enterprise (work tools)| Very high | Medium  | High     | Very high
```

What this overlap reveals: the key question is not "is the platform lock-in?"
but **"lock-in for whom?"** Lock-in severity is determined at the intersection
of structure and user.

## 9. Impact of This Case on the Framework

### What Was Tested

1. **The discriminant applies to non-territorial sovereignty** — territorial
   sovereignty (E-7) and network-based sovereignty (platform) can be placed on
   the same table.
2. **Composite lock-in occurs on platforms too** — lock-in emerges at the
   intersection of platform + payment + store + advertising + government
   authentication.
3. **The continuity of lock-in severity is demonstrated** — on the same
   platform, severity differs by user type; binary judgment is impossible.
4. **The three-layer data portability model is the real bottleneck** — only
   technical portability is satisfied; the absence of semantic and institutional
   portability makes forking impossible.
5. **The coercion of governance vs. coercion of the right of exit distinction
   works in practice** — it is made concrete that state regulation must focus on
   exit infrastructure, not platform internal policy.

### Newly Revealed Challenges

1. **Asymmetric cost of fork feasibility** — exit costs exist only for the user,
   and expulsion costs are nearly zero for the platform. The framework must
   address this asymmetry explicitly.
2. **Absence of judicial independence in redress procedures** — the reviewer is
   the same entity as the one who issued the disposition. The design of a
   third-party appeal body becomes a core prescription.
3. **Cascading suspension of business and personal accounts** — the structure
   in which a personal terms violation suspends the business account amplifies
   lock-in. Account separation protection is needed as a separate prescription.
4. **The technical challenge of social graph portability** — data can be
   exported, but the relationship graph cannot be replicated. The technical
   limits of fork feasibility must be addressed explicitly.

### Common Pattern Between E-7 and the Platform Case

Comparing the two cases reveals the common structure of composite lock-in:

1. **Each actor performs only its own role** — the state handles "residence
   order," the employer handles "employment contract." The platform handles
   "terms enforcement," the payment network handles "risk management."
2. **Lock-in at the intersection is no one's responsibility** — invisible to
   any single-sector audit.
3. **Prescriptions must dissolve the intersection simultaneously** — if only
   one side is resolved, a half-dissolved lock-in is still a lock-in.
4. **The enforcement actor paradox repeats** — the actor with the authority to
   adopt a remedy sees its own authority reduced by that remedy.

This common pattern demonstrates the framework's universality. The lock-in
discriminant applies to both territorial sovereignty (the state) and
non-territorial sovereignty (the platform), and the composite lock-in structure
arises identically in both domains.

## 10. Next Directions

The two cases (E-7, platform) have demonstrated the framework's applicability.
Next candidates:

- **Medical record non-portability (medical lock-in)** — the domain where the
  three-layer data portability model is most directly tested. The absence of
  institutional portability (layer 3) is directly tied to life.
- **Family care dependency (care lock-in)** — the domain where "those who
  cannot exit" are most clearly revealed. Economic dependency, custody,
  housing, and time combine into lock-in.
- **Educational credential monopoly (education lock-in)** — the domain where
  fork feasibility depends entirely on institutional portability. A case where
  technical portability exists but is meaningless.

These cases will further test how each of the framework's instruments (data
portability, lock-in severity, composite lock-in, fork feasibility) operates
in a different context.
