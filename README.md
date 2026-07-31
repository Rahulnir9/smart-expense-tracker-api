# Smart Expense Tracker API

A RESTful API built with **FastAPI** to manage personal expenses. The application allows users to create, view, filter, summarize, and delete expenses using JSON file storage.

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

# Installation

Create a virtual environment.

### Windows

```bash
python -m venv venv
```

Activate it.

```bash
venv\Scripts\activate
```

Install dependencies.

```bash
pip install -r requirements.txt
```

---

# Run the Server

Start the FastAPI server.

```bash
uvicorn src.main:app --reload
```

The server will start at:

```
http://127.0.0.1:8000
```

Swagger documentation:

```
http://127.0.0.1:8000/docs
```

---

# Run the Tests

Run all tests.

```bash
pytest
```

Verbose output.

```bash
pytest -v
```

Current status:

- **20 automated tests**
- **20 tests passing**

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

# Technologies Used

- Python
- FastAPI
- Pydantic
- Uvicorn
- Pytest