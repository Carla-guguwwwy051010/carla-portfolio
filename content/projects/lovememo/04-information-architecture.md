# LoveMemo｜Information Architecture

> Organizing a relationship across the past, present and future.

## 01. Architecture Objective

LoveMemo’s information architecture is built around one product idea:

> **A relationship is not a collection of isolated records. It is a continuous space connecting what two people are experiencing now, what they have lived through and what they hope to do next.**

The architecture therefore avoids organizing the product by content format alone. Instead of separating photos, notes, dates and lists into unrelated utilities, LoveMemo uses three temporal layers:

- **Home — Present**
- **Memories — Past**
- **Wish Jar — Future**

These three areas form the current Demo’s first-level structure.

---

## 02. Core Product Object

The primary product object is the **Relationship Space**.

In a future productized version, the space would be jointly accessed by two authorized users and would contain the relationship’s shared interactions, memories and wishes.

```text
Relationship Space
│
├── Present: Home
├── Past: Memories
└── Future: Wish Jar
```

The current front-end Demo visualizes this model, but does not yet implement real accounts, partner binding, persistent shared storage or production permission controls.

---

## 03. First-Level Navigation

### Home — The Present

Home represents the relationship’s current state. Its role is to provide an immediate sense of shared presence and surface lightweight interactions without asking users to enter a formal archive.

Home should answer:

> **What is happening between us now?**

Its architectural responsibilities are:

- Provide an emotional entry point to the shared space
- Surface lightweight, current relationship content
- Offer access to the other two temporal layers
- Create a reason to return before a large archive has accumulated

Home is not intended to become a generic dashboard containing every feature. Its value lies in immediacy and emotional orientation.

### Memories — The Past

Memories contains shared experiences that the couple wants to preserve and revisit.

Memories should answer:

> **What have we experienced together?**

Its architectural responsibilities are:

- Hold meaningful shared records
- Support browsing and revisiting over time
- Preserve context beyond a standalone image
- Receive records created directly or prompted by another relationship action

Memories is not positioned as a replacement for a complete photo library. It is a curated relationship layer focused on meaning and shared context.

### Wish Jar — The Future

Wish Jar holds things the two people hope to do together.

Wish Jar should answer:

> **What do we want to experience next?**

Its architectural responsibilities are:

- Preserve shared intentions before they disappear in chat
- Make future experiences visible within the relationship space
- Support movement from intention to completion
- Provide context for an optional memory after a wish is completed

Wish Jar should feel emotionally open rather than operationally rigid. It is not a conventional task manager and should not make shared plans feel like work assignments.

---

## 04. Current Demo Sitemap

The source Product Design defines the current product around the following high-level structure:

```text
LoveMemo Demo
│
├── Home
│   ├── Shared presence / current relationship content
│   ├── Lightweight daily interaction
│   └── Entry points to Memories and Wish Jar
│
├── Memories
│   ├── Memory overview / collection
│   ├── Memory detail
│   └── Memory creation or presentation interactions
│
└── Wish Jar
    ├── Wish overview / collection
    ├── Wish detail or state
    └── Wish creation or completion interactions
```

This sitemap describes the conceptual and navigable structure of the front-end Demo. It should not be interpreted as evidence of a production database, real two-account collaboration or complete backend lifecycle support.

---

## 05. Cross-Module Relationship

The product’s main architectural value does not come from the three sections existing independently. It comes from their ability to form a loop.

```text
               ┌───────────────┐
               │     HOME      │
               │    Present    │
               └───────┬───────┘
                       │
          presence and shared intention
                       │
                       ▼
               ┌───────────────┐
               │   WISH JAR    │
               │    Future     │
               └───────┬───────┘
                       │
                wish is experienced
                       │
                       ▼
               ┌───────────────┐
               │   MEMORIES    │
               │     Past      │
               └───────┬───────┘
                       │
              revisit and find meaning
                       │
                       └──────────────► new shared life
```

The desired relationship loop is:

**Shared life → expression or intention → experience → record → revisit → new shared life**

The current Demo communicates parts of this model. A fully connected lifecycle, including persistent state transitions and cross-account synchronization, belongs to future MVP implementation and validation.

---

## 06. Content Model

The architecture can be understood through four conceptual entities.

| Entity | Purpose | Temporal role | Current status |
|---|---|---|---|
| Relationship Space | Shared context containing the experience | Across time | Represented conceptually in the Demo; not a production shared account space |
| Lightweight Interaction | A small expression of current presence | Present | Represented through the Home experience |
| Memory | A meaningful shared experience preserved for later | Past | Represented through the Memories experience |
| Wish | A shared intention for a future experience | Future | Represented through the Wish Jar experience |

The information model deliberately avoids treating every object as an isolated post. Each object should retain its relationship context and, where relevant, its connection to another moment.

For example, a completed Wish may become the starting context for a Memory. This connection is a product direction; it should not be read as a fully implemented automated workflow unless verified in the running Demo.

---

## 07. Navigation Principles

### Organize by meaning, not file type

Users should enter a section based on what the moment means in the relationship, not whether the content is text, image or date data.

### Keep the first level stable

Home, Memories and Wish Jar provide a simple mental model. Secondary features should not continuously expand the primary navigation.

### Make time understandable

The past–present–future framework should be visible in the content and transitions, not only in explanatory copy.

### Support direct entry and continuity

Users should be able to create or view an item directly, while the product also offers natural transitions across modules.

### Avoid turning emotional content into administration

The architecture should minimize settings, categories and mandatory fields in the main relationship experience.

### Separate intimate space from account management

In a productized version, authentication, invitation, permissions and privacy controls are necessary. They should support the Relationship Space without becoming its emotional center.

---

## 08. Current Demo vs. Future Product Architecture

### Current front-end Demo

```text
Demo Entry
   │
   ▼
Home ───────── Memories ───────── Wish Jar
   └──────── navigable representative experiences ────────┘
```

The current Demo is responsible for:

- Communicating the past–present–future mental model
- Demonstrating the main navigation and representative interactions
- Making the Relationship Space concept understandable
- Supporting early product and usability feedback

### Future productized MVP

```text
Account / Authentication
          │
          ▼
Invitation and Partner Binding
          │
          ▼
Authorized Relationship Space
          │
          ├── Home
          ├── Memories
          └── Wish Jar
          │
          ▼
Persistent Data, Synchronization, Permissions and Privacy
```

The future MVP would additionally require:

- User identity and authentication
- Partner invitation and relationship binding
- Space creation and lifecycle management
- Persistent content storage
- Cross-account synchronization
- Object ownership and edit rules
- Relationship-space data isolation
- Removal, unbinding and exit behavior
- Privacy, security and recovery mechanisms

These layers are product requirements, not implemented Demo capabilities.

---

## 09. Architectural Boundaries

The initial architecture intentionally excludes or postpones areas that could dilute the core relationship loop.

### Not the current focus

- Public social feeds or discovery
- Multi-group or community spaces
- General-purpose chat replacement
- Full personal photo backup
- Complex project or task management
- Competitive scoring or relationship ranking
- A broad content marketplace
- Unverified AI-generated relationship interpretation

Keeping these outside the initial scope allows the product to test one central question: whether a private, two-person temporal space creates durable relationship value.

---

## 10. Key Architecture Decisions

### Decision 01 — Three primary areas instead of a feature grid

**Reasoning:** A feature grid explains what users can do, but not how those actions form a relationship story. Past, present and future provide a more coherent mental model.

### Decision 02 — Home as an emotional entry point

**Reasoning:** Memories and wishes may not change every day. Home needs to make the space feel alive without relying on archive growth alone.

### Decision 03 — Wish Jar separated from task management

**Reasoning:** A shared wish contains anticipation and emotional meaning. Productivity language, deadlines and completion pressure may weaken that value.

### Decision 04 — Memories as relationship context, not media storage

**Reasoning:** Photos are only one possible trace. The architecture should preserve why a moment mattered, not only what file was uploaded.

### Decision 05 — Cross-module continuity as the product advantage

**Reasoning:** Individual functions already exist in stronger specialist tools. LoveMemo’s opportunity lies in connecting them around the relationship.

---

## 11. Questions for Validation

The architecture remains a product hypothesis. Future testing should examine:

- Do users understand the distinction between Home, Memories and Wish Jar without explanation?
- Does the past–present–future model match how users think about shared life?
- Can users predict where a specific piece of content belongs?
- Does Home provide enough value when little shared content exists?
- Does connecting completed wishes to memories reduce recording effort?
- Do users want stricter categories or a more flexible shared timeline?
- How should ownership and permissions work when both partners can edit shared content?
- What happens to the space and its content when a partnership is unbound?

These questions should be answered through a real paired MVP and longer-term observation, not inferred from the front-end Demo alone.

---

## 12. Architecture Summary

LoveMemo’s information architecture translates its product strategy into a simple structure:

| Past | Present | Future |
|---|---|---|
| Memories | Home | Wish Jar |
| Revisit shared experiences | Feel current presence | Hold shared intentions |

The architecture is designed to turn three destinations into one continuing relationship loop.

> **The goal is not to organize more content. It is to help two people recognize continuity in the life they are building together.**

---

## 13. Evidence Boundary

This document is organized from **Our LoveMemo Product Design V1.0**, with supporting definitions from **Product Strategy V1.0** and **PRD V1.0**.

The **Home / Memories / Wish Jar** structure and past–present–future model reflect the source materials. Detailed backend layers, permissions and lifecycle requirements are presented only as future productization needs. No real account sharing, database persistence or production infrastructure is claimed for the current Demo.
