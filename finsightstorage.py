import sqlite3
import os
from typing import List, Optional
from .models import Expense

DB_PATH = os.getenv("FINSIGHT_DB", "finsight.db")

def get_connection() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            category TEXT NOT NULL,
            amount REAL NOT NULL,
            description TEXT DEFAULT '',
            date TEXT NOT NULL
        )
    """)
    conn.commit()
    return conn

def add_expense(expense: Expense) -> int:
    with get_connection() as conn:
        cursor = conn.execute(
            "INSERT INTO expenses (category, amount, description, date) VALUES (?, ?, ?, ?)",
            (expense.category, expense.amount, expense.description, expense.date.isoformat())
        )
        return cursor.lastrowid

def get_all_expenses() -> List[Expense]:
    with get_connection() as conn:
        rows = conn.execute("SELECT * FROM expenses ORDER BY date DESC").fetchall()
        return [Expense(**dict(row)) for row in rows]

def get_expense_by_id(expense_id: int) -> Optional[Expense]:
    with get_connection() as conn:
        row = conn.execute("SELECT * FROM expenses WHERE id = ?", (expense_id,)).fetchone()
        return Expense(**dict(row)) if row else None

def delete_expense(expense_id: int) -> bool:
    with get_connection() as conn:
        cursor = conn.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))
        return cursor.rowcount > 0