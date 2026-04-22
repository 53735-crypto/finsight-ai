from fastapi import FastAPI, HTTPException
from typing import List
from finsight.models import Expense, Insight
from finsight import storage, analytics, ai_categorizer

app = FastAPI(title="FinSight AI API", version="1.0.0", description="REST API for intelligent expense tracking")

@app.post("/expenses/", response_model=dict)
def create_expense(expense: Expense):
    eid = storage.add_expense(expense)
    return {"id": eid, "message": "Expense added"}

@app.get("/expenses/", response_model=List[Expense])
def list_expenses():
    return storage.get_all_expenses()

@app.get("/analytics/total")
def get_total():
    return {"total": analytics.total_expenses(storage.get_all_expenses())}

@app.get("/analytics/insights", response_model=List[Insight])
def get_insights():
    return analytics.generate_insights(storage.get_all_expenses())

@app.get("/ai/summary")
def ai_summary():
    expenses = storage.get_all_expenses()
    return {"summary": ai_categorizer.generate_ai_summary(expenses)}