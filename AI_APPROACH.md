# AI_APPROACH.md

AI tools were used selectively to accelerate development, explore testing ideas, and assist with debugging during implementation.

The final architecture, API behavior, validation logic, and testing strategy were reviewed and verified manually before being incorporated into the project.

---

## How AI Was Used

AI was used as a supporting tool in the following areas:

* Discussing REST API design approaches
* Reviewing validation requirements
* Generating ideas for edge cases and negative test scenarios
* Troubleshooting MySQL and Flask configuration issues
* Suggesting improvements to automated test coverage

Example prompts included:


Suggest edge cases for a task management REST API.

What validation scenarios should be tested for CRUD operations?

How can state verification be implemented in integration tests?


---

## How AI Helped Testing

The most valuable use of AI was in expanding the testing strategy.

AI helped identify additional scenarios such as:

* Missing required fields
* Invalid date formats
* Invalid priority values
* Invalid status values
* Non-existing task operations
* Boundary validation cases

These suggestions were manually reviewed and converted into automated pytest integration tests.

---

## Manual Development and Verification

The core implementation was completed manually, including:

* Flask API development
* Database schema creation
* SQLAlchemy model implementation
* MySQL configuration
* Endpoint implementation


All APIs were manually tested using Postman.

Database changes were verified through MySQL Workbench to ensure correct persistence behavior.

---

## Issues Identified During Testing

Automated tests helped identify several implementation issues, including:

* Missing validation in update operations
* Invalid date handling during updates
* Invalid priority updates being accepted
* Invalid title data types during updates

These defects were fixed manually after being discovered through automated test execution.

---
AI was used in reviewing approaches, and expanding test coverage.
