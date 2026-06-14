#  Smart Task & Notification Service

This project is a REST API backend for managing tasks and simulating task notifications. The service supports task creation, retrieval, updates, deletion, filtering, and notification payload generation.

The application is built using Flask and MySQL and includes automated integration tests using pytest.

---

## Technology Stack

* Python
* Flask
* MySQL
* SQLAlchemy
* Pytest
* Requests
* Docker

---

## Features

### Task Management

* Create a task
* Retrieve all tasks
* Filter tasks by priority
* Update task details and status
* Delete tasks

### Notification Service

* Simulated notification endpoint
* Notification payload generation and validation

### Validation

* Mandatory field validation
* Priority validation
* Status validation
* Date format validation
* Data type validation

### Monitoring

* Health check endpoint
* Application logging

---

## API Endpoints

### Create Task

```http
POST /tasks
```

Request Body:

```json
{
  "title": "Complete Assignment",
  "description": "Finish task",
  "priority": "High",
  "dueDate": "2026-06-20"
}
```

---

### Get All Tasks

```http
GET /tasks
```

---

### Filter Tasks By Priority

```http
GET /tasks?priority=High
```

---

### Update Task

```http
PUT /tasks/{id}
```

Example:

```json
{
  "status": "Completed"
}
```

---

### Delete Task

```http
DELETE /tasks/{id}
```

---

### Trigger Notification

```http
POST /tasks/{id}/notify
```

---

### Health Check

```http
GET /health
```

---

## Project Structure

```text
smart-task-service/
│
├── app.py
├── config.py
├── models.py
├── requirements.txt
│
├── tests/
│   ├── test_create_task.py
│   ├── test_get_tasks.py
│   ├── test_update_task.py
│   ├── test_delete_task.py
│   ├── test_notify_task.py
│   ├── test_filter_tasks.py
│   ├── test_validation.py
│   ├── test_negative_cases.py
│   └── test_health.py
│
├── Dockerfile
├── docker-compose.yml
├── README.md
└── AI_APPROACH.md
```

---

## Database Setup

Create a MySQL database:

```sql
CREATE DATABASE taskdb;
```

Create a user:

```sql
CREATE USER 'taskuser'@'localhost'
IDENTIFIED BY 'Task123';

GRANT ALL PRIVILEGES ON taskdb.*
TO 'taskuser'@'localhost';

FLUSH PRIVILEGES;
```

---

## Local Setup

### Clone Repository

```bash
git clone https://github.com/B-Meghana-Reddy/smart-task-service.git
cd smart-task-service
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run Application

```bash
python app.py
```

Application URL:

```text
http://127.0.0.1:5000
```

---

## Run Automated Tests

### Running Tests

Start the Flask application in one terminal:

```bash
python app.py
```

Open a second terminal and execute:

```bash
pytest -v
```

The test suite performs end-to-end integration testing by sending real HTTP requests to the running Flask service.

### Generate Coverage Report

```bash
pytest --cov=. --cov-report=html
```

The coverage report will be generated inside the `htmlcov/` directory.

Open:

```text
htmlcov/index.html
```

to view the report.

---

## Test Results

The project includes:

* 23 automated integration tests
* CRUD endpoint testing
* Notification endpoint testing
* Health endpoint testing
* Validation testing
* Negative testing
* State verification testing
* Filtering functionality testing

All tests execute against a running Flask application and a real MySQL database to validate end-to-end behavior.

---

## Docker Execution

Build and start containers:

```bash
docker-compose up --build
```

Stop containers:

```bash
docker-compose down
```

---

## Logging

The application uses Python logging to record:

* Task creation
* Task updates
* Task deletion
* Notification requests
* Validation failures

---
