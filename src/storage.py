
import json
from pathlib import Path
from .models import Expense

DATA_FILE = Path("expenses.json")


def read_expenses() -> list[Expense]:
  
    if not DATA_FILE.exists():
        return []

    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            data = json.load(file)

        return [Expense(**expense) for expense in data]

    except json.JSONDecodeError:
        return []


def write_expenses(expenses: list[Expense]) -> None:
    
    with DATA_FILE.open("w", encoding="utf-8") as file:
        json.dump(
            [expense.model_dump(mode="json") for expense in expenses],
            file,
            indent=4,
        )