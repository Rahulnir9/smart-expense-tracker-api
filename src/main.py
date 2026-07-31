from fastapi import FastAPI

from .routes import router

app = FastAPI(
    title="Smart Expense Tracker API",
    description="REST API for managing personal expenses.",
    version="1.0.0",
)

app.include_router(router)