# LogiTrack API 
> **A high-performance Logistics & Delivery Tracking REST API built with Django.**

LogiTrack is a production-ready backend system designed to handle real-time delivery management. It leverages asynchronous task processing, containerized infrastructure, and professional-grade security patterns.

---

## System Architecture



The system is architected for scalability and separation of concerns:
* **Django REST Framework:** Core API logic following the **Service Layer pattern**.
* **PostgreSQL:** Relational database for persistent and structured data.
* **Celery + Redis:** Distributed task queue for asynchronous processing (e.g., status updates, notifications).
* **Docker & Docker Compose:** Full stack containerization for environment parity.
* **AWS EC2:** Cloud hosting with optimized security groups and networking.

---

## Key Features

* **Secure Authentication:** Implemented via **JWT (JSON Web Tokens)** for stateless and secure communication.
* **Background Jobs:** Offloaded heavy processing (Email/Logs) to **Celery** workers to keep API response times under 200ms.
* **API Documentation:** Fully interactive documentation using **Swagger/OpenAPI** (available at `/api/docs/`).
* **Data Integrity:** Strict validation layers and relational mapping for complex delivery workflows.
* **CI/CD Pipeline:** Automated testing and quality assurance via **GitHub Actions**.

---

## Tech Stack

| Category | Technology |
| :--- | :--- |
| **Language** | Python 3.11+ |
| **Framework** | Django / Django REST Framework |
| **Database** | PostgreSQL |
| **Caching/Queue** | Redis |
| **Workers** | Celery |
| **Server** | Gunicorn |
| **Cloud/DevOps** | AWS (EC2), Docker, GitHub Actions |

---

## Installation & Local Setup

### Prerequisites
* Docker & Docker Compose installed.

### Steps
1. **Clone the repository:**
   ```bash
   git clone https://github.com/keyles-Py/LogiTrack-API
   cd logitrack-api
2. **Set up environment variables: Create a .env file in the root directory:**
   ```bash
   DEBUG=True
   SECRET_KEY=your_secret_key
   POSTGRES_DB=logitrack
   POSTGRES_USER=admin
   POSTGRES_PASSWORD=password
   DATABASE_URL=postgres://admin:password@db:5432/logitrack
   CELERY_BROKER_URL=redis://redis:6379/
3. **Run with Docker Compose:**
   ```bash
   docker-compose up --build
   
  The API will be available at ``http://localhost:8000.``
## Deployment
The project is currently deployed on AWS EC2. The deployment pipeline is automated:

1. Code pushed to main branch.

2. GitHub Actions runs unit tests and linters.

3. Upon success, the application is updated on the AWS instance using Docker Compose.

## Development Journey
I maintained a daily log of the technical challenges and decisions made during the construction of this API. 
You can read the full dev diary here: [JOURNAL.md](./JOURNAL.md)

## Contact

Keiner Mendoza - [linkedin](https://www.linkedin.com/in/keinermendoza/) - [E-mail](keynerismo@gmail.com) - [Project Link](https://github.com/keyles-Py/LogiTrack-API)
