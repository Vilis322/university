# User Stories — Zoo Management System

---

## User Story 1

| Title: View animal feed budget breakdown | Priority: High | Estimate: 3 SP |
|:-----------------------------------------|:---------------|:----------------|

**User Story:**

As a **zookeeper**,
I want **to view the budget breakdown for my animal (total budget, amount spent, amount reserved for pending deliveries, amount remaining)**,
so that **I can plan future feed orders within the available budget**.

**Acceptance Criteria:**

**AC 1.1**
Given a zookeeper is assigned to an animal with a monthly budget,
When the zookeeper views the budget,
Then the system shows total budget, amount spent, amount reserved for pending deliveries, and amount not spent.

**AC 1.2**
Given an animal has pending feed orders that have not yet arrived,
When the zookeeper views the budget,
Then the pending orders' totals are shown as "reserved" and are not deducted from the spent amount.

**AC 1.3**
Given a zookeeper is not assigned to an animal this month,
When they try to view that animal's budget,
Then access is denied with an appropriate error message.

---

## User Story 2

| Title: Order feed and record invoice | Priority: High | Estimate: 5 SP |
|:-------------------------------------|:---------------|:----------------|

**User Story:**

As a **zookeeper**,
I want **to order feed from an authorized dealer and record the invoice total with an expected delivery date**,
so that **the order is tracked in the system and the amount is properly reserved in the budget**.

**Acceptance Criteria:**

**AC 2.1**
Given a zookeeper is responsible for an animal and the order total does not exceed the remaining budget,
When the zookeeper places an order with an authorized dealer,
Then the order is recorded with the invoice total and expected delivery date, and the amount is reserved in the budget.

**AC 2.2**
Given a zookeeper tries to order from a dealer that is not on the authorized dealers list,
When they attempt to place the order,
Then the system rejects the order with an error message.

**AC 2.3**
Given the order total would exceed the remaining budget (total minus spent minus reserved),
When the zookeeper checks the planned order,
Then the system warns that the budget would be exceeded.

---

## User Story 3

| Title: Request and process additional funds | Priority: Medium | Estimate: 5 SP |
|:--------------------------------------------|:-----------------|:----------------|

**User Story:**

As a **zoo director**,
I want **to review and respond to budget increase requests from zookeepers**,
so that **I can ensure animals are properly fed while maintaining financial control over the zoo's budget**.

**Acceptance Criteria:**

**AC 3.1**
Given a zookeeper has submitted a budget increase request with a short statement,
When the zoo director views their messages,
Then the request is displayed with the statement and a link to the corresponding animal's budget.

**AC 3.2**
Given the zoo director grants a budget increase request,
When they enter the increase amount and confirm,
Then the budget for the corresponding animal is increased by that amount, and all zookeepers responsible for the animal receive a notification marked "additional funds granted on request".

**AC 3.3**
Given the zoo director denies a budget increase request,
When they write a denial statement and confirm,
Then the requesting zookeeper receives a message with the denial reason, and the budget overview shows "additional funds were requested but not granted" with a link to the request.
