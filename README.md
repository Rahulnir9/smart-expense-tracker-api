# Smart Expense Tracker API

A RESTful API built using **Python** and **FastAPI** to manage personal expenses. The application allows users to create, view, filter, summarize, and delete expenses while storing data in a local JSON file.


---

## Features

- Add a new expense
- View all expenses
- Filter expenses by category
- Calculate total expenses
- Calculate total expenses by category
- Delete an expense
- Monthly expense summary
- Input validation with Pydantic
- JSON-based storage
- Automated tests using Pytest

---

## Project Structure

```
your-repo/
│
├── README.md
├── AI_NOTES.md
├── requirements.txt
├── pytest.ini
├── expenses.json
│
├── src/
│   ├── __init__.py
│   ├── exceptions.py
│   ├── main.py
│   ├── models.py
│   ├── routes.py
│   ├── service.py
│   └── storage.py
│
└── tests/
    └── test_api.py
```

---
## Prerequisites

Before running this project, ensure you have the following installed:

- Python 3.10 or later (developed and tested with Python 3.13)
- Git

# Installation


### 1. Clone the repository

```bash
git clone https://github.com/Rahulnir9/smart-expense-tracker-api
cd smart-expense-tracker-api
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
python -m pip install -r requirements.txt
```

---

## Run the Server

Start the FastAPI development server:

```bash
python -m uvicorn src.main:app --reload
```

The server will be available at:

```
http://127.0.0.1:8000
```

Swagger API documentation:

```
http://127.0.0.1:8000/docs
```

ReDoc documentation:

```
http://127.0.0.1:8000/redoc
```

---

## Run the Tests

Run all automated tests:

```bash
python -m pytest
```


For verbose output:

```bash
python -m pytest -v
```

## Test Coverage

The project includes **20 automated test cases** covering:

- Expense creation
- Duplicate expense handling
- Input validation
- Category filtering
- Total calculations
- Monthly summary
- Expense deletion
- Edge cases

All tests pass successfully.

Current status:

- **20 automated tests**
- **All tests passing**

---

# API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/expenses` | Create a new expense |
| GET | `/expenses` | Get all expenses |
| GET | `/expenses/category/{category}` | Get expenses by category |
| GET | `/expenses/total` | Get total expenses |
| GET | `/expenses/total/{category}` | Get total for a category |
| DELETE | `/expenses/{expense_id}` | Delete an expense |
| GET | `/expenses/summary/monthly` | Monthly expense summary |

---

# Example Request

**POST /expenses**

```json
{
  "id": 1,
  "title": "Lunch",
  "amount": 250,
  "category": "Food",
  "date": "2026-07-31"
}
```

---

# Design

The project follows a layered architecture:

- **Routes** handle HTTP requests.
- **Service layer** contains business logic.
- **Storage layer** manages JSON file operations.
- **Pydantic models** validate request and response data.
- **Custom exceptions** provide meaningful error handling.

---

## Technologies Used

- Python 3.13
- FastAPI (REST API Framework)
- Uvicorn (ASGI Server)
- Pydantic (Data Validation)
- Pytest (Automated Testing)
