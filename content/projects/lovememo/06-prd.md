# LoveMemo｜Product Requirements Document

**Document type:** Portfolio PRD Summary  
**Version:** V1.0  
**Product stage:** Runnable front-end Demo / Future shared MVP definition  
**Source:** LoveMemo PRD V1.0, Product Strategy V1.0, User Research & Product Insight V1.0, Product Design V1.0

> LoveMemo is a private Relationship Space designed to help shared life leave traces naturally.

---

## 01. Document Purpose

This document defines LoveMemo’s product logic, initial scope and productization requirements while preserving a clear distinction between:

- **[DEMO]** — represented or operable in the current React/Vite/Tailwind front-end prototype
- **[MVP]** — required for a real two-person product but not currently implemented
- **[HYPOTHESIS]** — a product direction that still requires validation
- **[TBD]** — a rule or implementation detail not confirmed by the source materials

The current Demo should not be interpreted as a launched multi-user product.

---

## 02. Product Background

Couples already create many shared digital traces: messages, photos, plans, places and small expressions of care. These traces are distributed across tools organized around communication, media, tasks or events.

The resulting problem is not a lack of content. It is the absence of a coherent, private space organized around **“us.”**

At the same time, deliberate recording can become burdensome. A product intended to preserve emotional meaning may lose that value if it repeatedly asks users to upload, categorize or complete relationship tasks.

LoveMemo explores whether one relationship-centered product structure can connect:

- The **present** — lightweight shared presence
- The **past** — meaningful memories
- The **future** — wishes and shared intentions

---

## 03. Product Vision

> **Create a private space whose value grows as two people live, remember and look forward together.**

LoveMemo does not aim to replace messaging, cloud photo storage or productivity tools. It provides a relationship-centered layer that connects the meaning scattered across them.

---

## 04. Product Goals

### Demo goals

1. **[DEMO]** Communicate the Relationship Space concept.
2. **[DEMO]** Validate whether users understand the Home / Memories / Wish Jar structure.
3. **[DEMO]** Demonstrate representative core interactions.
4. **[DEMO]** Collect early feedback on value, comprehension and recording effort.

### MVP goals

1. **[MVP]** Enable two real users to enter the same authorized private space.
2. **[MVP]** Persist and synchronize shared content across accounts.
3. **[MVP]** Support a complete shared loop from intention to memory.
4. **[MVP]** Define clear permissions, privacy and relationship-space lifecycle rules.
5. **[HYPOTHESIS]** Determine whether the space creates enough ongoing value to support return behavior.

---

## 05. Non-Goals

The initial version is not intended to become:

- A public social network
- A general messaging replacement
- A complete photo-backup service
- A project-management or task product
- A couple-therapy or diagnostic service
- A competitive relationship scoring system
- A multi-community collaboration platform
- An autonomous AI relationship advisor

These boundaries protect the central product hypothesis from uncontrolled feature expansion.

---

## 06. Target Users

LoveMemo focuses on two people in an ongoing intimate relationship who already produce shared digital traces but lack a coherent place to preserve and revisit them.

The early research included **8 participants over approximately one week**. Findings are treated as early product signals rather than a validated market profile.

### Core needs

- Feel the other person’s presence in everyday life
- Preserve meaningful moments without heavy recording work
- Keep shared intentions from disappearing in conversation
- Revisit a relationship history with emotional context
- Participate as co-owners of a private space
- Understand and control access to intimate content

---

## 07. Core Product Model

The product is organized around one conceptual parent object:

```text
Relationship Space
│
├── Home       — Present
├── Memories   — Past
└── Wish Jar   — Future
```

### Core loop

```text
Shared life
    ↓
Lightweight expression or shared wish
    ↓
Experience together
    ↓
Preserve a memory
    ↓
Revisit shared history
    ↓
New shared life
```

The Demo represents this product model. The real shared space and persistent lifecycle require MVP infrastructure.

---

## 08. Scope Summary

| Capability | Current Demo | Future MVP | Notes |
|---|---:|---:|---|
| Home / Memories / Wish Jar navigation | Yes | Yes | Core information architecture |
| Representative relationship content | Yes | Yes | Demo content does not imply real shared data |
| Representative creation interactions | Yes | Yes | Production persistence and failures require MVP work |
| Account registration and sign-in | No | Required | Authentication method TBD |
| Partner invitation and binding | No | Required | Invitation rules TBD |
| Shared Relationship Space | Conceptual | Required | Must be authorized and isolated |
| Persistent database | No | Required | Technology and data schema TBD |
| Cross-account synchronization | No | Required | Real-time requirements TBD |
| Permissions and ownership rules | No | Required | Editing/deletion model TBD |
| Relationship exit / unbinding | No | Required | Content consequences TBD |
| AI-assisted recording | Not confirmed | Exploratory | Opt-in hypothesis; not baseline MVP |
| Public feed or community | No | No | Explicitly outside initial scope |

---

## 09. Functional Requirements

### 9.1 Home

#### Purpose

Provide the emotional entry point to the current relationship space and a lightweight reason to return.

#### Requirements

- **[DEMO]** The user can enter Home as a primary destination.
- **[DEMO]** Home presents representative current relationship content.
- **[DEMO]** The user can navigate from Home to Memories and Wish Jar.
- **[DEMO]** The experience demonstrates lightweight relationship interaction.
- **[MVP]** Home content must load from the authorized Relationship Space.
- **[MVP]** New shared content must synchronize between both participants.
- **[MVP]** Loading, empty, failure and offline states must be defined.
- **[HYPOTHESIS]** A lightweight daily note or expression may create an immediate return trigger.

#### Acceptance direction

- Primary destinations are understandable without extensive instruction.
- Empty Home does not imply that the relationship is incomplete.
- Interaction does not require unnecessary form completion.
- A user never sees content from another Relationship Space.

---

### 9.2 Memories

#### Purpose

Preserve and revisit meaningful shared experiences with relationship context.

#### Requirements

- **[DEMO]** The user can access a Memories overview.
- **[DEMO]** The user can open representative memory content.
- **[DEMO]** The experience communicates memory creation or presentation.
- **[MVP]** Users can create and persist a memory.
- **[MVP]** Users can view memory details after saving.
- **[MVP]** Supported media, upload limits and processing rules must be defined.
- **[MVP]** Save failure must preserve user input and offer recovery.
- **[MVP]** Editing and deletion permissions must be explicit.
- **[TBD]** Search, filters, tags and sorting are not confirmed as baseline MVP requirements.

#### Product rules

- A memory should preserve meaning, not only a file.
- Required fields should remain minimal.
- Memory creation must not force users to classify every moment.
- The product must not invent events or emotional interpretations.

---

### 9.3 Wish Jar

#### Purpose

Hold shared intentions and make future experiences visible within the relationship.

#### Requirements

- **[DEMO]** The user can access a Wish Jar overview.
- **[DEMO]** The user can explore representative wish content and interactions.
- **[MVP]** An authorized user can add a wish to the shared space.
- **[MVP]** Both participants can view the shared wish.
- **[MVP]** A wish can move through a defined lifecycle.
- **[TBD]** Exact states beyond active and experienced/completed require confirmation.
- **[TBD]** Assignment, deadlines and reminders are not baseline requirements.

#### Product rules

- A wish is a shared intention, not a productivity task.
- The interface should avoid default pressure, scoring or overdue language.
- Participation rules must not make one partner the automatic project manager.

---

### 9.4 Wish-to-Memory Transition

#### Purpose

Reduce recording effort by reusing the context of an experience that began as a shared wish.

#### Conceptual flow

```text
Wish is marked as experienced
        ↓
Optional prompt to preserve the moment
        ├── Not now → keep the wish state
        └── Continue
                ↓
Reuse relevant wish context
                ↓
User adds, reviews or confirms memory content
                ↓
Save to Memories
```

#### Requirements

- **[HYPOTHESIS]** The transition may lower the blank-page burden.
- **[MVP]** If implemented, the prompt must remain optional.
- **[MVP]** Relevant context may be reused only transparently.
- **[MVP]** Users must review the memory before sharing or saving.
- **[TBD]** Automatic field mapping and lifecycle behavior require validation.

The complete connected flow is not claimed as a production capability of the Demo.

---

## 10. Account and Shared-Space Requirements

This section applies to future productization.

### 10.1 Authentication

- **[MVP]** Users must create an account or sign in.
- **[MVP]** Sessions must be handled securely.
- **[MVP]** Account recovery and identity-change behavior must be defined.
- **[TBD]** Login method, verification method and recovery mechanism.

### 10.2 Invitation and binding

- **[MVP]** One user can create a Relationship Space and invite a partner.
- **[MVP]** The invited person explicitly accepts before binding occurs.
- **[MVP]** Invalid, expired, cancelled and declined invitations require clear states.
- **[TBD]** Invitation expiry and resend limits.
- **[TBD]** Whether one account can belong to more than one active space.

### 10.3 Authorization and isolation

- **[MVP]** Only authorized participants can access a Relationship Space.
- **[MVP]** All reads and writes must be scoped to the correct space.
- **[MVP]** Space identifiers must not expose another couple’s data.
- **[MVP]** Access changes must propagate reliably after unbinding or account changes.

### 10.4 Shared ownership

- **[MVP]** The interface must show which actions are available to each participant.
- **[TBD]** Who can edit or delete content created by the other partner.
- **[TBD]** Whether some actions require mutual confirmation.
- **[TBD]** Export and retention rights after leaving the space.

---

## 11. Privacy and Trust Requirements

Relationship content may be intimate. Privacy is a core product property, not only a technical checklist.

- **[MVP]** Shared content must be private by default.
- **[MVP]** Users must know who can access each space.
- **[MVP]** Invitations require explicit consent.
- **[MVP]** Sensitive actions such as leaving, unbinding or destructive deletion require confirmation.
- **[MVP]** The product must communicate the consequences of access changes.
- **[MVP]** Personal data collection should be limited to what the product needs.
- **[MVP]** Security, retention, deletion and recovery policies require formal definition before launch.
- **[TBD]** Legal, regional and age-related requirements.

---

## 12. AI-Assisted Recording — Future Exploration

AI-assisted recording emerged as a possible way to reduce documentation effort. It is not treated as a confirmed current feature or mandatory MVP requirement.

### Product principle

> Use AI to remove work, not manufacture intimacy.

### If explored, the system should

- **[HYPOTHESIS]** Draft or organize content from context users have chosen to provide.
- Require explicit user initiation or consent.
- Clearly distinguish generated suggestions from user-authored content.
- Allow complete review, editing and rejection.
- Never save or share generated content without confirmation.
- Avoid inventing events, motives or emotional conclusions.
- Explain how source content is used and protected.

### Not in scope

- Autonomous relationship diagnosis
- Relationship scoring presented as objective truth
- Unreviewed automatic publication
- Fabricated memories or inferred private events

---

## 13. Key States

Every production content surface should account for:

| State | Required behavior |
|---|---|
| Loading | Communicate progress without showing unrelated cached data |
| Empty | Explain value and offer one low-effort next action |
| Ready | Present authorized shared content and available actions |
| Editing | Preserve entered content during recoverable interruptions |
| Saving | Prevent accidental duplicate submission |
| Success | Confirm completion and show where content now lives |
| Failure | Explain the problem, preserve input and offer retry |
| Offline | Clarify what is available and whether changes are pending |
| Unauthorized | Do not expose content; provide a safe next step |

The Demo may visually represent only a subset of these. Complete behavior is an MVP requirement.

---

## 14. Non-Functional Requirements

The source materials define productization needs at a high level. Numeric thresholds remain TBD.

### Security

- Authentication and authorization must protect each Relationship Space.
- Sensitive data must be protected in transit and at rest.
- Destructive and access-changing operations require auditability appropriate to risk.

### Reliability

- User-created content must not silently disappear.
- Failed writes must be recoverable where possible.
- Synchronization conflicts require a defined strategy.

### Performance

- Primary navigation and shared content should load within an acceptable mobile experience.
- Media handling should not block essential interaction.
- **[TBD]** Numeric latency and availability targets.

### Accessibility

- Core actions should be keyboard and screen-reader understandable where applicable.
- Text, controls, state changes and contrast should meet the selected accessibility standard.
- **[TBD]** Target standard and audit process.

### Compatibility

- **[TBD]** Supported browsers, devices and operating-system versions.

---

## 15. Measurement Framework

The early materials do not establish production analytics results. The following is a proposed validation framework.

### Activation

- Both users successfully join the same Relationship Space
- Each partner completes at least one meaningful shared action

### Contribution

- Percentage of active spaces with participation from both users
- Distribution of contributions between partners
- Completion and abandonment points in memory and wish creation

### Relationship loop

- Wishes later marked as experienced
- Experienced wishes followed by optional memory creation
- Memories revisited after creation

### Retention

- Return at appropriate weekly and monthly intervals
- Whether return is associated with partner activity, archive value or reminders

### Qualitative signals

- Perceived recording effort
- Sense of shared ownership
- Emotional value of revisiting
- Pressure or obligation created by prompts
- Trust in privacy and assisted features

No target numbers or achieved results are claimed because they are not confirmed in the source materials.

---

## 16. MVP Acceptance Framework

A future MVP should not be considered complete based only on screen implementation.

### Shared access

- Two users can explicitly join the same space.
- Unauthorized users cannot access it.
- Invitation failures are understandable and recoverable.

### Shared content

- Authorized users can create, view and revisit supported content.
- Data persists across sessions.
- Updates appear reliably for both participants.
- Failures do not silently discard user input.

### Ownership and trust

- Users understand who can edit, delete and retain content.
- Leaving or unbinding communicates consequences before confirmation.
- Private content is not public by default.

### Core value loop

- Users can move between Home, Wish Jar and Memories.
- A shared intention can reach a defined experienced state.
- If the wish-to-memory path is included, it remains optional and preserves user control.

---

## 17. Release Approach

### Stage 0 — Current concept Demo

- Validate product framing and information architecture
- Observe comprehension and interaction friction
- Collect early product signals

### Stage 1 — Technical shared-space foundation

- Authentication
- Partner invitation and binding
- Relationship-space data model
- Persistent storage and authorization

### Stage 2 — Core shared MVP

- Productized Home, Memories and Wish Jar
- Cross-account synchronization
- Complete loading, empty, success and failure states
- Ownership, deletion and exit rules

### Stage 3 — Retention validation

- Observe real two-person contribution over a longer period
- Test lightweight return triggers
- Test the wish-to-memory transition
- Evaluate participation imbalance and perceived pressure

### Stage 4 — Assisted capture exploration

- Explore opt-in AI assistance only after the core loop and trust model are understood
- Validate effort reduction, control and authenticity before broader use

This sequence prioritizes evidence over feature expansion.

---

## 18. Risks

| Risk | Why it matters | Initial response |
|---|---|---|
| Recording feels like work | Undermines the core emotional value | Minimize required input; use contextual, optional prompts |
| Only one partner participates | Creates emotional and operational imbalance | Measure reciprocity; avoid blame-based reminders |
| Cold-start space feels empty | Archive value has not accumulated | Provide lightweight present-tense value through Home |
| Product duplicates existing tools | Users have little reason to adopt another app | Focus on continuity between wishes, experiences and memories |
| Privacy expectations are unclear | Intimate content requires high trust | Make authorization, ownership and exit rules explicit |
| AI content feels synthetic | Could weaken authenticity | Keep assistance opt-in, transparent and user-controlled |
| Demo is mistaken for a finished product | Creates false implementation claims | Label all current and future capabilities consistently |

---

## 19. Open Questions

- What authentication method is appropriate for the target market?
- Can an account belong to more than one Relationship Space?
- What is the exact invitation expiry and cancellation behavior?
- Who can edit or delete shared content?
- What happens to content after unbinding or account deletion?
- Which fields are truly required for a useful memory or wish?
- Should completed wishes remain in Wish Jar, appear in Memories or both?
- What return behavior represents relationship value rather than notification compliance?
- How should uneven participation be handled without creating pressure?
- What user context, if any, may be used for assisted recording?
- Which privacy, retention and safety policies are required before release?

These questions should remain visible rather than being resolved through unsupported assumptions.

---

## 20. Product Success Definition

The first meaningful success condition is not the number of features implemented or records created.

LoveMemo succeeds at the MVP stage if:

> **Two real users can safely share one private space, contribute with low effort and find increasing value in returning to their own relationship context.**

Whether that value persists for one month or one year remains the central question for future validation.

---

## 21. Evidence Boundary

This portfolio PRD consolidates the supplied LoveMemo materials. It intentionally avoids inventing endpoints, database schemas, business targets, pricing, retention figures or finished production behavior.

The current implementation is described only as a runnable **React/Vite/Tailwind front-end Demo**. Accounts, database persistence, invitation and binding, cross-account synchronization, permission controls, space isolation, production privacy mechanisms and AI-assisted recording are identified as future requirements, open decisions or hypotheses unless the source documents explicitly establish otherwise.
