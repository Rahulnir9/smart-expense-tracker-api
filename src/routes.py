"""
API routes for the Smart Expense Tracker API.
"""

from fastapi import APIRouter, HTTPException, status

from .exceptions import (
    DuplicateExpenseError,
    ExpenseNotFoundError,
)
from .models import (
    Expense,
    TotalResponse,
    CategoryTotalResponse,
    MonthlySummaryResponse,
)
from .service import ExpenseService

router = APIRouter()


@router.post(
    "/expenses",
    response_model=Expense,
    status_code=status.HTTP_201_CREATED,
)
def create_expense(expense: Expense):
    """
    Add a new expense.
    """
    try:
        return ExpenseService.add_expense(expense)
    except DuplicateExpenseError as e:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=str(e),
        )


@router.get(
    "/expenses",
    response_model=list[Expense],
)
def get_all_expenses():
    """
    Get all expenses.
    """
    return ExpenseService.get_all_expenses()


@router.get(
    "/expenses/category/{category}",
    response_model=list[Expense],
)
def get_expenses_by_category(category: str):
    """
    Filter expenses by category.
    """
    return ExpenseService.get_expenses_by_category(category)


@router.get(
    "/expenses/total",
    response_model=TotalResponse,
)
def get_total():
    """
    Get total expenses.
    """
    return TotalResponse(
        total=ExpenseService.calculate_total()
    )


@router.get(
    "/expenses/total/{category}",
    response_model=CategoryTotalResponse,
)
def get_category_total(category: str):
    """
    Get total expenses for a category.
    """
    return CategoryTotalResponse(
        category=category,
        total=ExpenseService.calculate_total(category),
    )


@router.delete(
    "/expenses/{expense_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_expense(expense_id: int):
    """
    Delete an expense.
    """
    try:
        ExpenseService.delete_expense(expense_id)
    except ExpenseNotFoundError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e),
        )


@router.get(
    "/expenses/summary/monthly",
    response_model=MonthlySummaryResponse,
)
def get_monthly_summary():
    """
    Get monthly expense summary.
    """
    return MonthlySummaryResponse(
        summary=ExpenseService.monthly_summary()
    )


@router.get("/")
def root():
    """
    Root endpoint.
    """
    return {
        "message": "Smart Expense Tracker API is running."
    }