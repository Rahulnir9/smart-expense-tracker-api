"""
Custom exceptions for the Smart Expense Tracker API.
"""

class ExpenseError(Exception):
    """
    Base exception for all expense-related errors.
    """


class DuplicateExpenseError(ExpenseError):
    """
    Raised when an expense with the same ID already exists.
    """


class ExpenseNotFoundError(ExpenseError):
    """
    Raised when an expense cannot be found.
    """