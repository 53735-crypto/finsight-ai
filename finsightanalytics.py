from typing import List, Dict
from collections import defaultdict
from .models import Expense, Insight
import math

def total_expenses(expenses: List[Expense]) -> float:
    return sum(e.amount for e in expenses)

def most_expensive(expenses: List[Expense]) -> Optional[Expense]:
    return max(expenses, key=lambda e: e.amount) if expenses else None

def category_breakdown(expenses: List[Expense]) -> Dict[str, float]:
    breakdown = defaultdict(float)
    for e in expenses:
        breakdown[e.category] += e.amount
    return dict(breakdown)

def detect_anomalies(expenses: List[Expense], threshold: float = 2.0) -> List[Expense]:
    if len(expenses) < 3:
        return []
    amounts = [e.amount for e in expenses]
    mean = sum(amounts) / len(amounts)
    variance = sum((x - mean) ** 2 for x in amounts) / len(amounts)
    std = math.sqrt(variance) if variance > 0 else 1.0
    return [e for e in expenses if abs(e.amount - mean) > threshold * std]

def generate_insights(expenses: List[Expense]) -> List[Insight]:
    insights = []
    if not expenses:
        return insights

    total = total_expenses(expenses)
    breakdown = category_breakdown(expenses)
    top_cat = max(breakdown, key=breakdown.get)

    insights.append(Insight(
        title="Spending Overview",
        message=f"Total spent: ₹{total:.2f}. Highest category: {top_cat} (₹{breakdown[top_cat]:.2f})",
        type="info"
    ))

    anomalies = detect_anomalies(expenses)
    if anomalies:
        insights.append(Insight(
            title="Unusual Spending Detected",
            message=f"{len(anomalies)} transaction(s) significantly deviate from your average. Review for errors or fraud.",
            type="warning"
        ))

    return insights