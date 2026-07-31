"""
Business logic for the Smart Expense Tracker API.
"""

from collections import defaultdict

from .exceptions import (
    DuplicateExpenseError,
    ExpenseNotFoundError,
)
from .models import Expense
from .storage import (
    read_expenses,
    write_expenses,
)


class ExpenseService:
    """
    Handles all expense-related business logic.
    """

    @staticmethod
    def add_expense(expense: Expense) -> Expense:
        """
        Add a new expense.
        """

        expenses = read_expenses()

        if any(existing.id == expense.id for existing in expenses):
            raise DuplicateExpenseError(
                f"Expense with ID {expense.id} already exists."
            )

        expenses.append(expense)

        write_expenses(expenses)

        return expense

    @staticmethod
    def get_all_expenses() -> list[Expense]:
        """
        Return all expenses.
        """

        return read_expenses()

    @staticmethod
    def get_expenses_by_category(
        category: str,
    ) -> list[Expense]:
        """
        Return expenses for a category.
        """

        expenses = read_expenses()

        return [
            expense
            for expense in expenses
            if expense.category.lower() == category.lower()
        ]

    @staticmethod
    def calculate_total(
        category: str | None = None,
    ) -> float:
        """
        Calculate total expenses.
        """

        expenses = read_expenses()

        if category:

            expenses = [
                expense
                for expense in expenses
                if expense.category.lower() == category.lower()
            ]

        return sum(expense.amount for expense in expenses)

    @staticmethod
    def delete_expense(
        expense_id: int,
    ) -> None:
        """
        Delete an expense.
        """

        expenses = read_expenses()

        updated_expenses = [
            expense
            for expense in expenses
            if expense.id != expense_id
        ]

        if len(updated_expenses) == len(expenses):
            raise ExpenseNotFoundError(
                f"Expense with ID {expense_id} not found."
            )

        write_expenses(updated_expenses)

    @staticmethod
    def monthly_summary() -> dict[str, float]:
        """
        Return monthly expense totals.
        """

        expenses = read_expenses()

        summary = defaultdict(float)

        for expense in expenses:

            month = expense.date.strftime("%Y-%m")

            summary[month] += expense.amount

        return dict(summary)