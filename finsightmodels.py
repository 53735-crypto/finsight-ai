from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class Expense(BaseModel):
    id: Optional[int] = None
    category: str
    amount: float
    description: str = ""
    date: datetime = Field(default_factory=datetime.now)

    class Config:
        json_schema_extra = {
            "example": {"category": "Food", "amount": 450.0, "description": "Grocery shopping"}
        }

class Insight(BaseModel):
    title: str
    message: str
    type: str = "info"  # info, warning, success