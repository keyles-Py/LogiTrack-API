# LogiTrack API: Backend Developer Journey

This repository is a technical journal of my evolution as a Backend Developer. Here I document not only the code, but also the design decisions, the challenges encountered, and the solutions implemented.

## Day 1: 11 Jan 2026 - Phase 1: Project Foundation & Business Logic
### Objective
Design and implement the core of a logistics management system (LogiTrack API) using Python and Django, ensuring data integrity from the model.
### 1. Database Design
I started the project with a data-first approach, designing an entity-relationship (ER) diagram and a logical design to normalize user, vehicle, and delivery information.

ER diagram

<img src="https://cdn.imgchest.com/files/b117b615adc6.png" alt="ER diagram" width="500"/>

Logical design

<img src="https://cdn.imgchest.com/files/abd043917101.png" alt="Logic diagram" width="500"/>

### 2. Implementation Highlights

* Django Models: I implemented the data architecture using Django ORM, extending the capabilities of the user system.
* Business Logic: I developed a custom validation to ensure that deliveries are not assigned to vehicles undergoing maintenance.
* Admin Customization: We configure the administrative panel for quick fleet management.

### based on these diagrams, I created the models using Django and used them via the Django admin page also implemetating the logic to avoid assigning a delivery to a vehicle that is in maintenance.

## Day 2: 13 Jan 2026 - Phase 2: Building the RESTful API

- DRF Integration: I installed and configured Django REST Framework to transform the project into a decoupled API.

- Nested Serializers: I implemented nested serialization to improve the data consumption experience (DX), allowing vehicle details to be obtained in the same delivery request.

- API Safety: I confirmed that the business rules defined in Phase 1 remain intact when interacting through REST endpoints.

## Day 3: 15 Jan 2026 - Phase 3: Containerization & Infrastructure and testing

Docker Integration: I implemented a Dockerfile to standardize the execution environment.

Orchestration: I used Docker Compose to set up a microservices ecosystem. (App + DB).

Production Grade DB: I migrated from SQLite to PostgreSQL, configuring volumes for data persistence.

Environment Variables: I implemented the use of .env files to decouple sensitive configuration from the source code.

Principle of least privilege: I ensured that database credentials are not tracked in version control (Git), following OWASP and Django security best practices.

Container Management: I learned how to interact with isolated services using the docker-compose exec command. I understood that the database in Postgres lives in a separate ecosystem and that migrations must be executed within the context of the application container to synchronize the ORM with the actual database engine.

Automated Testing: I implemented my first APITestCase to ensure that business rules are unbreakable.

TDD Mindset: I learned that testing is not a waste of time, but an investment in stability. Validating expected failures (such as the vehicle in maintenance) is as important as validating success.

Isolated Testing: The tests are run in an ephemeral environment within Docker, ensuring that the production database is not contaminated with test data.

## Day 4: 17 Jan 2026 - Phase 4: Interactive Documentation, JWT Authentication & Permissions

OpenAPI 3.0: I implemented drf-spectacular to generate a standardized API schema.

Self-Documented Code: I realized that a good backend not only works, but is also easy to use. Interactive documentation with Swagger reduces friction between the backend and frontend teams.

Interactive Testing: Now the QA or Frontend team can test business logic (such as blocking vehicles undergoing maintenance) directly from the documentation UI.

Stateless Auth: I implemented JSON Web Tokens (JWT) to handle authentication without sessions on the server, ideal for scalability.

Granular Permissions: I differentiated between public read permissions and actions restricted to administrators (Staff) by overwriting get_permissions.

Security Best Practices: I learned how to manage access and refresh tokens to maintain API security without forcing the user to log in constantly.

Bearer Token Authentication: I implemented the industry standard for sending JWT credentials in HTTP headers.

Performance Tuning (N+1 Problem): I used select_related to optimize database queries using SQL JOINs, drastically reducing API latency on large lists.