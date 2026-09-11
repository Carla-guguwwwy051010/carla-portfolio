# LoveMemo｜Project Background

> A private relationship space that helps shared life leave traces naturally.

## 01. Project Overview

LoveMemo is a personal 0→1 product exploration focused on intimate relationships.

The project began with a simple observation: two people may share many moments, plans, photos and small promises, but those fragments usually live across chat histories, photo albums, notes, calendars and maps. Each tool stores a piece of life; none of them is designed around the relationship itself.

LoveMemo explores a different product unit: not an individual account, a photo collection or a task list, but a private **Relationship Space** jointly shaped by two people.

Its core proposition is not “help users record more.” It is:

> **Let shared life leave traces naturally — and make those traces meaningful when revisited.**

---

## 02. Why I Started This Project

Many meaningful moments in a relationship are ordinary: a short note, a place visited together, a plan mentioned in passing, or something the two people hope to do later. These moments are emotionally valuable, yet they are easy to lose because the tools used to capture them are fragmented and organized for other purposes.

- Chats are optimized for immediate communication; meaningful details quickly disappear in the timeline.
- Photo albums preserve media, but rarely retain the shared context around it.
- Notes and calendars can store plans, but often feel like personal productivity tools.
- Couple-oriented apps may offer check-ins or decorative interactions, but those mechanisms can turn emotional expression into another task.

This led to the initial design question:

> **How might a product help two people preserve, continue and revisit their shared life without making “recording the relationship” feel like work?**

The question shifted the project away from building another memory album and toward exploring how a relationship can become the organizing context of a digital product.

---

## 03. Core Problem

The project identified three connected problems.

### Shared information is fragmented

Memories, plans and everyday expressions are distributed across different tools. Users may have plenty of content, but there is no coherent space that represents “our life together.”

### Intentional recording creates pressure

When recording requires users to repeatedly decide what to write, upload or categorize, a warm emotional activity can become a maintenance task. The more a product asks users to “complete,” the more easily it competes with the life it is meant to preserve.

### Existing tools separate past, present and future

Photos describe what happened; messages capture what is happening; notes and calendars hold what might happen next. The relationship itself, however, moves continuously across all three.

LoveMemo therefore treats the problem not as a lack of features, but as a lack of an appropriate product structure: a space centered on **“us”**, where everyday interaction, accumulated memories and future intentions can form one continuous loop.

---

## 04. Product Opportunity

The opportunity is to connect three temporal layers of a relationship:

| Layer | User need | LoveMemo direction |
|---|---|---|
| Present | Feel the other person’s presence in daily life | A shared Home for lightweight, immediate interaction |
| Past | Preserve and revisit meaningful shared moments | Memories organized within the relationship context |
| Future | Hold wishes and turn intentions into shared experiences | A Wish Jar for things the two people want to do together |

This structure became the foundation of the product’s first-level information architecture: **Home / Memories / Wish Jar**.

Together, they support a longer relationship loop:

**Shared life → lightweight interaction or intention → experience → record → revisit → inspire new shared life**

The opportunity is not to replace chats, photo albums, calendars or maps. LoveMemo instead explores a relationship-centered layer that can connect the emotional meaning scattered across those tools.

---

## 05. Current Prototype Status

The current deliverable is a runnable front-end Demo built with **React, Vite and Tailwind CSS**. It is used to communicate and test the product concept, core information architecture and key interaction ideas.

### Implemented in the current Demo

- A navigable front-end experience organized around **Home / Memories / Wish Jar**
- Representative interfaces and interactions for the core concept
- A visible product structure connecting the present, past and future of a relationship
- A prototype suitable for early experience feedback and product discussion

### Not implemented in the current Demo

- Real user accounts and authentication
- A persistent production database
- Real invitation and partner-binding mechanisms
- Cross-account, real-time shared data
- Permission management and relationship-space isolation
- Production-grade security, privacy and operational capabilities

The Demo should therefore be understood as a **concept and interaction prototype**, not as a launched multi-user product. Any locally demonstrated content or interaction does not prove that account-level sharing or production infrastructure already exists.

---

## 06. Future MVP / Productization Direction

The future MVP described in the PRD would move LoveMemo from a front-end concept toward a genuine two-person shared experience. That requires product infrastructure beyond the current Demo, including:

- Account creation and authentication
- Invitation, acceptance and relationship binding
- A shared space accessible by two authorized users
- Persistent storage and synchronization of shared content
- Clear ownership, permissions and space-level data isolation
- Privacy and security rules appropriate for intimate content

These are **planned productization capabilities**, not current implementation claims.

The MVP is not intended to maximize feature count. Its purpose is to validate whether a real shared loop can be established: two people enter the same private space, contribute to it with low effort, and find enough ongoing relationship value to return.

---

## 07. Goals and Boundaries

### Project goals

1. Explore whether **Relationship Space** can work as the core product unit.
2. Connect everyday presence, shared memories and future wishes in one understandable structure.
3. Reduce the effort and psychological pressure associated with intentional recording.
4. Use a working prototype to collect early product signals and refine the product hypothesis.
5. Define a credible path from a front-end Demo to a real two-person MVP.

### Current boundaries

- This project does not claim market validation.
- Early feedback comes from a small exploratory group and represents **early product signals**, not statistically generalizable conclusions.
- The current Demo does not validate long-term retention, relationship outcomes or technical scalability.
- AI-assisted recording and other lower-effort capture ideas remain product directions unless explicitly implemented and tested.
- The project does not attempt to replace every tool couples already use; it focuses on the relationship context connecting shared traces.

---

## 08. My Product Thinking

The most important shift in this project was moving from **feature design** to **relationship-value design**.

At first, it is easy to imagine the product as a collection of useful modules: notes, memories, wishes and shared activities. But a feature list does not explain why two people would return after one week, one month or one year. For a relationship product, retention cannot rely only on reminders, streaks or more content-entry tasks. It must come from the growing value of the shared space itself.

This changed how I evaluated the product:

- From “How can users record more?” to “How can meaningful traces emerge with less effort?”
- From “What features should a couple app include?” to “What makes this space belong specifically to these two people?”
- From “Can the interface be completed?” to “Can a sustainable shared loop be formed?”
- From “Does early feedback sound positive?” to “Which hypotheses have actually been tested, and which remain assumptions?”

LoveMemo is therefore both a product prototype and an ongoing product question:

> **Can a digital space become more valuable over time because it carries the history, intentions and everyday presence of a relationship?**

The current Demo establishes the first expression of that idea. The next stage is not simply feature expansion, but validation of retention, contribution balance, privacy expectations and the real long-term value of the relationship space.

---

## 09. Evidence Note

This background document is synthesized from the project’s four source materials: **LoveMemo PRD V1.0**, **Product Strategy V1.0**, **User Research & Product Insight V1.0**, and **Product Design V1.0**.

All descriptions deliberately distinguish between:

- what is visible or operable in the current front-end Demo;
- what was observed as an early product signal;
- and what remains a future MVP, productization requirement or hypothesis to validate.

No production capability, user scale, behavioral result or market conclusion is implied beyond those source materials.
