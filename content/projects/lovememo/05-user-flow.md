# LoveMemo｜User Flow

> From shared intention to shared experience, memory and renewed connection.

## 01. Flow Objective

LoveMemo’s user flow is designed around an ongoing relationship loop rather than a single conversion endpoint.

The product does not end when a user creates a wish or saves a memory. Its intended value comes from connecting those moments:

```text
Shared Life
    ↓
Lightweight Expression or Shared Intention
    ↓
Experience Together
    ↓
Record a Meaningful Trace
    ↓
Revisit the Relationship History
    ↓
Create New Shared Life
```

The current front-end Demo communicates representative parts of this experience. Real two-person access, synchronized state and persistent shared data belong to the future productized MVP.

---

## 02. User Roles

### Current Demo

The Demo is navigated as a representative relationship experience. It does not implement two authenticated users with independently controlled accounts.

### Future MVP

The productized version requires two participant roles within one private Relationship Space:

- **Initiating partner** — creates or enters an account, creates the space and sends an invitation
- **Invited partner** — accepts the invitation and joins the same space

After successful binding, both should become authorized participants rather than permanently unequal “owner” and “guest” roles. Exact creation, editing, deletion and exit permissions remain product decisions to define and validate.

---

## 03. Current Demo Entry Flow

The current Demo begins inside the product concept rather than with a real account lifecycle.

```text
Open Demo
    ↓
Enter Home
    ↓
Understand the current relationship context
    ↓
Choose a destination
    ├── View or interact with Home content
    ├── Browse Memories
    └── Browse Wish Jar
```

### What this flow validates

- Whether the overall concept is understandable
- Whether the three primary areas are distinguishable
- Whether users can navigate representative screens
- Whether the past–present–future structure feels coherent

### What this flow does not validate

- Registration or authentication completion
- Invitation acceptance or partner binding
- Two-device synchronization
- Shared editing and conflict handling
- Persistent data across real accounts
- Permission, privacy or relationship-exit behavior

---

## 04. Future MVP Onboarding and Partner Binding

This flow is required for productization but is not a claim about the current Demo.

```text
New User Opens LoveMemo
          ↓
Create Account / Sign In
          ↓
Create a Relationship Space
          ↓
Generate and Send Invitation
          ↓
Partner Opens Invitation
          ↓
Partner Creates Account / Signs In
          ↓
Review and Accept Invitation
          ↓
System Binds Both Accounts to One Space
          ↓
Both Partners Enter Shared Home
```

### Required exception paths

```text
Invitation invalid or expired
          └── Explain status → Request a new invitation

Invitation sent to the wrong person
          └── Cancel invitation → Generate another invitation

User already belongs to another active space
          └── Explain restriction → Provide a safe resolution path

Invitation declined
          └── Do not create binding → Inform initiating user appropriately
```

Exact eligibility rules, invitation expiry, identity verification and multi-space policy are not confirmed in the current source materials and should remain open requirements.

---

## 05. Home Flow — Feel the Present

Home is the emotional entry point. The desired flow should be short and low-pressure.

```text
Enter Shared Home
        ↓
See Current Relationship Content
        ↓
Choose an Action
        ├── View a lightweight note or expression
        ├── Leave a lightweight expression
        ├── Continue to Memories
        └── Continue to Wish Jar
```

### Design intention

- Provide immediate emotional value
- Make the other person’s presence visible
- Avoid forcing users to create a formal record on every visit
- Offer natural entry points to the past and future

Early research suggested that a small daily note could become a reason to return. This is an early signal, not validated retention evidence.

---

## 06. Memory Browsing Flow — Revisit the Past

```text
Enter Memories
       ↓
Browse Shared Memory Collection
       ↓
Select a Memory
       ↓
View Memory Detail and Context
       ↓
Return to Collection or Continue Exploring
```

### User goal

> “I want to revisit something meaningful we experienced together.”

### Flow principles

- Make browsing possible without requiring a known search target
- Preserve relationship context, not only media
- Keep the return path to the memory collection clear
- Avoid presenting the archive as a productivity log

The Demo can represent this browsing model. Production search, filtering, synchronization and storage behavior require separate implementation.

---

## 07. Memory Creation Flow

### Direct creation path

```text
Enter Memories
       ↓
Choose to Add a Memory
       ↓
Provide the Minimum Necessary Content
       ↓
Review
       ↓
Save
       ↓
Memory Appears in the Shared Collection
```

### Design principle

Memory creation should minimize the blank-page problem. Only information necessary to preserve the meaning of the moment should be required.

### Future product requirements

- Persistent save state
- Media upload and processing
- Draft, retry and failure handling
- Shared visibility and synchronization
- Clear editing and deletion permissions
- User control over assisted or generated content

These requirements are not evidence that the current Demo already supports a complete production creation lifecycle.

---

## 08. Wish Jar Flow — Hold the Future

### Create a wish

```text
Enter Wish Jar
       ↓
Choose to Add a Wish
       ↓
Describe a Shared Intention
       ↓
Review
       ↓
Save to the Shared Wish Jar
```

### Revisit a wish

```text
Enter Wish Jar
       ↓
Browse Existing Wishes
       ↓
Open a Wish
       ↓
Return, Update or Mark as Experienced
```

### User goal

> “I want us to remember something we hope to do together.”

The flow should avoid making a wish feel like an assigned task. Deadlines, ownership and completion pressure should not be introduced by default without evidence that they support the emotional use case.

---

## 09. Core Cross-Module Flow

The most important flow connects Wish Jar and Memories.

```text
Create or Save a Wish
          ↓
Wish Remains Visible in the Shared Space
          ↓
Two People Have the Experience
          ↓
Mark Wish as Experienced
          ↓
Optional Prompt: Preserve This Moment?
          ├── Not Now → Keep completed state without pressure
          └── Continue
                 ↓
          Reuse Known Wish Context
                 ↓
          Add or Confirm Memory Content
                 ↓
          Save to Memories
                 ↓
          Revisit Later
```

### Why this flow matters

A wish already contains part of the story. Reusing that context could reduce the effort of starting a memory from nothing.

### Evidence boundary

Early research identified this as a promising way to lower recording burden. The complete transition, automatic context reuse and its effect on contribution behavior remain hypotheses for future implementation and testing.

---

## 10. Assisted Recording Direction

AI-assisted or automated recording is a future exploration, not an established current feature.

A responsible conceptual flow would be:

```text
Existing User-Provided Context
          ↓
User Chooses Assistance
          ↓
System Produces a Draft or Suggestion
          ↓
User Reviews and Edits
          ↓
User Explicitly Confirms
          ↓
Save to Shared Space
```

### Guardrails

- Assistance should be opt-in
- Generated text should remain editable
- Nothing should be shared without user confirmation
- The system should not invent events or emotional conclusions
- Source context and privacy expectations should be clear
- Users need a way to discard assisted content

The product opportunity is to reduce recording work, not manufacture intimacy on the users’ behalf.

---

## 11. Return Loop

LoveMemo requires value at different stages of content accumulation.

```text
Early Stage
Lightweight presence creates a reason to return
          ↓
Growing Stage
Wishes and memories create shared continuity
          ↓
Mature Stage
Accumulated relationship context may become valuable to revisit
```

This lifecycle is a product hypothesis. The early study did not validate one-month or one-year retention.

Potential return triggers must therefore be evaluated carefully:

- A partner leaves a lightweight expression
- A shared wish becomes relevant
- Users choose to preserve a recent experience
- A past memory becomes meaningful to revisit

Notifications should support real relationship context rather than manufacture urgency or guilt.

---

## 12. Empty, Error and Uneven-Participation States

### Empty relationship space

```text
Enter an Empty Section
       ↓
Explain Its Relationship Value
       ↓
Offer One Clear, Low-Effort First Action
```

Empty states should not imply that the relationship is incomplete because no content has been added.

### Save or synchronization failure — future MVP

```text
User Submits Content
       ↓
Save Fails
       ↓
Preserve User Input
       ↓
Explain the Failure Clearly
       ↓
Retry or Save as Draft
```

### Partner has not participated

```text
One Partner Contributes
       ↓
Other Partner Has Not Responded
       ↓
Avoid Public Scoring or Blame
       ↓
Offer a Neutral Reminder Only When Appropriate
```

Participation imbalance is not merely a notification problem. It may affect the emotional meaning of the product and requires research before intervention rules are defined.

---

## 13. Relationship-Space Exit Flow — Future Requirement

Because LoveMemo may contain intimate shared content, leaving a relationship space requires explicit product rules.

```text
User Requests to Leave / Unbind
          ↓
Explain Content and Access Consequences
          ↓
User Reviews Available Options
          ↓
Explicit Confirmation
          ↓
Apply Access and Retention Rules
          ↓
Notify the Other Participant Safely
```

Open decisions include:

- Whether users can export content they contributed
- Whether shared content requires mutual handling
- What each user retains after unbinding
- Whether a cooling-off or recovery period is appropriate
- How to protect users in sensitive or unsafe circumstances

The current Demo does not implement this lifecycle. It is a necessary productization and trust requirement.

---

## 14. Flow Principles

### Every action should have relationship meaning

The product should avoid adding steps simply to increase activity metrics.

### Creation should be optional and recoverable

Users should be able to pause, cancel or return without losing meaningful input.

### Cross-module transitions should reduce work

Moving from Wish Jar to Memories should reuse relevant context rather than ask users to repeat it.

### Both partners need clear agency

Shared space does not mean ambiguous ownership. Viewing, editing, deletion and exit require understandable rules.

### Emotional safety matters in system behavior

Notifications, completion states and participation cues should avoid blame, comparison or pressure.

### The Demo and productized flow must remain distinguishable

Representative navigation can validate comprehension. It cannot validate real synchronization, security, retention or two-person behavior.

---

## 15. Validation Plan

Future testing should examine the flow at three levels.

### Comprehension

- Can users identify where to leave a present expression, save a memory and create a wish?
- Do users understand what happens after a wish is marked as experienced?
- Are Demo interactions mistaken for real shared functionality?

### Effort

- How long does it take to create a meaningful memory?
- Which fields cause hesitation or abandonment?
- Does reusing wish context lower perceived recording effort?

### Relationship behavior

- Do both partners participate?
- What produces a genuine return rather than notification-driven compliance?
- How does the space feel when contribution is uneven?
- Does accumulated content become more valuable over time?

No conclusion in these areas should be claimed before a real paired MVP and longer observation period.

---

## 16. Flow Summary

LoveMemo’s core flow can be reduced to one sentence:

> **Help two people carry a shared intention into lived experience, preserve it with minimal effort and return to it as part of an evolving relationship history.**

The current Demo establishes the navigable concept. The future MVP must prove that the loop works with two real users, persistent shared data and trustworthy control.

---

## 17. Evidence Boundary

This document is derived from **Our LoveMemo Product Design V1.0**, **LoveMemo PRD V1.0**, **Product Strategy V1.0** and **User Research & Product Insight V1.0**.

The broad relationship loop and the **Home / Memories / Wish Jar** experience reflect the source materials. Account onboarding, partner binding, synchronization, exception handling, assisted recording and exit management are clearly marked as future MVP requirements or design directions. They are not presented as capabilities already implemented in the current front-end Demo.
