from fastapi import FastAPI, HTTPException, Query, status

from src.models import Expense, ExpenseCreate
from src.storage import load_expenses, save_expenses, get_next_id

app = FastAPI(
    title="Smart Expense Tracker API",
    description="REST API to manage personal expenses.",
    version="1.0.0"
)

@app.post("/expenses", response_model=Expense, status_code=status.HTTP_201_CREATED)
def add_expense(expense: ExpenseCreate):

    expenses = load_expenses()

    expense_id = get_next_id(expenses)

    new_expense = {
        "id": expense_id,
        "title": expense.title,
        "amount": expense.amount,
        "category": expense.category,
        "date": str(expense.date)
    }

    expenses.append(new_expense)

    save_expenses(expenses)

    return new_expense

@app.get("/expenses", response_model=list[Expense])
def get_expenses(category: str | None = Query(default=None)):

    expenses = load_expenses()

    if category:
        filtered = [
            expense
            for expense in expenses
            if expense["category"].lower() == category.lower()
        ]
        return filtered

    return expenses

@app.get("/expenses/total")
def get_total_expenses(category: str | None = Query(default=None)):

    expenses = load_expenses()

    if category:
        total = sum(
            expense["amount"]
            for expense in expenses
            if expense["category"].lower() == category.lower()
        )

        return {
            "category": category,
            "total": total
        }

    total = sum(expense["amount"] for expense in expenses)

    return {
        "total": total
    }

@app.delete("/expenses/{expense_id}")
def delete_expense(expense_id: int):

    expenses = load_expenses()

    for expense in expenses:
        if expense["id"] == expense_id:

            expenses.remove(expense)

            save_expenses(expenses)

            return {
                "message": "Expense deleted successfully"
            }

    raise HTTPException(
        status_code=404,
        detail="Expense not found"
    )