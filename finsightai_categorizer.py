import re
from typing import Dict, List

# Rule-based fallback + mock LLM structure (works offline, API-ready)
KEYWORD_MAP: Dict[str, List[str]] = {
    "Food": ["restaurant", "cafe", "swiggy", "zomato", "grocery", "food", "starbucks", "mcdonald"],
    "Travel": ["uber", "ola", "metro", "bus", "train", "flight", "petrol", "fuel", "taxi"],
    "Shopping": ["amazon", "flipkart", "mall", "store", "shop", "clothing", "electronics"],
    "Bills": ["electricity", "water", "internet", "wifi", "recharge", "subscription", "netflix"],
    "Health": ["pharmacy", "hospital", "doctor", "medicine", "clinic", "lab"],
    "Entertainment": ["movie", "cinema", "game", "concert", "spotify", "youtube"]
}

def categorize_transaction(description: str, amount: float) -> str:
    desc_lower = description.lower()
    for category, keywords in KEYWORD_MAP.items():
        if any(kw in desc_lower for kw in keywords):
            return category
    return "Miscellaneous"

def generate_ai_summary(expenses: List) -> str:
    # Mock LLM summary (replace with actual API call in production)
    total = sum(e.amount for e in expenses)
    cats = set(e.category for e in expenses)
    return (
        f"📊 AI Insight: You spent ₹{total:.2f} across {len(cats)} categories. "
        f"Consider setting a monthly envelope budget for {max(set(e.category for e in expenses), key=lambda c: sum(e.amount for e in expenses if e.category == c))} "
        f"to optimize cash flow. Your spending pattern shows consistent daily transactions."
    )