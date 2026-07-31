from pathlib import Path

from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)

DATA_FILE = Path("expenses.json")


def setup_function():
    """
    Reset the JSON file before each test.
    """
    DATA_FILE.write_text("[]", encoding="utf-8")


def add_sample_expense(
    expense_id=1,
    title="Lunch",
    amount=250,
    category="Food",
    date="2026-07-31",
):
    return client.post(
        "/expenses",
        json={
            "id": expense_id,
            "title": title,
            "amount": amount,
            "category": category,
            "date": date,
        },
    )


# -------------------------
# CREATE
# -------------------------

def test_add_expense():
    response = add_sample_expense()

    assert response.status_code == 201
    assert response.json()["title"] == "Lunch"


def test_duplicate_expense():
    add_sample_expense()

    response = add_sample_expense()

    assert response.status_code == 409


def test_invalid_negative_amount():
    response = client.post(
        "/expenses",
        json={
            "id": 2,
            "title": "Coffee",
            "amount": -100,
            "category": "Food",
            "date": "2026-07-31",
        },
    )

    assert response.status_code == 422


def test_missing_required_field():
    response = client.post(
        "/expenses",
        json={
            "id": 2,
            "amount": 100,
            "category": "Food",
            "date": "2026-07-31",
        },
    )

    assert response.status_code == 422


# -------------------------
# READ
# -------------------------

def test_get_all_expenses():
    add_sample_expense()

    response = client.get("/expenses")

    assert response.status_code == 200
    assert len(response.json()) == 1


def test_get_empty_expenses():
    response = client.get("/expenses")

    assert response.status_code == 200
    assert response.json() == []


def test_filter_existing_category():
    add_sample_expense()

    response = client.get("/expenses/category/Food")

    assert response.status_code == 200
    assert len(response.json()) == 1


def test_filter_case_insensitive():
    add_sample_expense()

    response = client.get("/expenses/category/food")

    assert response.status_code == 200
    assert len(response.json()) == 1


def test_filter_non_existing_category():
    add_sample_expense()

    response = client.get("/expenses/category/Travel")

    assert response.status_code == 200
    assert response.json() == []


# -------------------------
# TOTAL
# -------------------------

def test_total_expenses():
    add_sample_expense()
    add_sample_expense(
        expense_id=2,
        title="Movie",
        amount=500,
        category="Entertainment",
    )

    response = client.get("/expenses/total")

    assert response.status_code == 200
    assert response.json()["total"] == 750


def test_category_total():
    add_sample_expense()
    add_sample_expense(
        expense_id=2,
        title="Movie",
        amount=500,
        category="Entertainment",
    )

    response = client.get("/expenses/total/Food")

    assert response.status_code == 200
    assert response.json()["total"] == 250


def test_total_for_unknown_category():
    add_sample_expense()

    response = client.get("/expenses/total/Travel")

    assert response.status_code == 200
    assert response.json()["total"] == 0


# -------------------------
# DELETE
# -------------------------

def test_delete_expense():
    add_sample_expense()

    response = client.delete("/expenses/1")

    assert response.status_code == 204

    response = client.get("/expenses")

    assert response.json() == []


def test_delete_non_existing_expense():
    response = client.delete("/expenses/100")

    assert response.status_code == 404


# -------------------------
# MONTHLY SUMMARY
# -------------------------

def test_monthly_summary():
    add_sample_expense(
        expense_id=1,
        amount=250,
        date="2026-07-15",
    )

    add_sample_expense(
        expense_id=2,
        amount=500,
        date="2026-07-20",
    )

    add_sample_expense(
        expense_id=3,
        amount=300,
        date="2026-08-01",
    )

    response = client.get("/expenses/summary/monthly")

    summary = response.json()["summary"]

    assert response.status_code == 200
    assert summary["2026-07"] == 750
    assert summary["2026-08"] == 300


# -------------------------
# ROOT
# -------------------------

def test_root():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["message"] == "Smart Expense Tracker API is running."

# -------------------------
# EXTRA EDGE CASES
# -------------------------

def test_zero_amount():
    response = client.post(
        "/expenses",
        json={
            "id": 10,
            "title": "Free Item",
            "amount": 0,
            "category": "Misc",
            "date": "2026-07-31",
        },
    )

    assert response.status_code == 422


def test_empty_title():
    response = client.post(
        "/expenses",
        json={
            "id": 11,
            "title": "",
            "amount": 100,
            "category": "Food",
            "date": "2026-07-31",
        },
    )

    assert response.status_code == 422


def test_total_when_no_expenses():
    response = client.get("/expenses/total")

    assert response.status_code == 200
    assert response.json()["total"] == 0


def test_monthly_summary_when_empty():
    response = client.get("/expenses/summary/monthly")

    assert response.status_code == 200
    assert response.json()["summary"] == {}
    