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

