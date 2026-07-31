from datetime import date
from pydantic import BaseModel, Field

class Expense(BaseModel):
    id: int = Field(
        ...,
        gt=0,
        description="Unique expense ID"
    )
    title: str = Field(
        ...,
        min_length=1,
        max_length=100,
        description="Expense title"
    )
    amount: float = Field(
        ...,
        gt=0,
        description="Expense amount"
    )
    category: str = Field(
        ...,
        min_length=1,
        max_length=50,
        description="Expense category"
    )
    date: date

class TotalResponse(BaseModel):
    """Represents the total expense amount."""

    total: float = Field(..., description="Total expense amount")


class CategoryTotalResponse(BaseModel):
    """Represents the total expense amount for a category."""

    category: str = Field(..., description="Expense category")
    total: float = Field(..., description="Total expense amount")


class MonthlySummaryResponse(BaseModel):
    """Represents monthly expense totals."""

    summary: dict[str, float] = Field(
        ...,
        description="Monthly expense totals"
    )