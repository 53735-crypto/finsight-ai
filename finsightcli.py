import typer
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from datetime import datetime
from .models import Expense
from . import storage, analytics, ai_categorizer

app = typer.Typer(name="finsight", help="🤖 FinSight AI - Intelligent Personal Finance Assistant")
console = Console()

@app.command()
def add(description: str, amount: float, category: str = None):
    """Add a new expense. AI auto-categorizes if category omitted."""
    if not category:
        category = ai_categorizer.categorize_transaction(description, amount)
    expense = Expense(category=category, amount=amount, description=description)
    eid = storage.add_expense(expense)
    console.print(f"✅ Added expense #{eid}: {category} | ₹{amount} | {description}")

@app.command()
def history(limit: int = 10):
    """View recent expenses."""
    expenses = storage.get_all_expenses()[:limit]
    if not expenses:
        console.print("📭 No expenses recorded yet.")
        return
    table = Table(title="💸 Recent Expenses")
    table.add_column("ID", style="cyan")
    table.add_column("Date", style="green")
    table.add_column("Category", style="magenta")
    table.add_column("Amount", style="yellow")
    table.add_column("Description", style="white")
    for e in expenses:
        table.add_row(str(e.id), e.date.strftime("%Y-%m-%d"), e.category, f"₹{e.amount:.2f}", e.description)
    console.print(table)

@app.command()
def insights():
    """Generate AI-powered spending insights."""
    expenses = storage.get_all_expenses()
    if not expenses:
        console.print("📭 Add expenses first to generate insights.")
        return
    for insight in analytics.generate_insights(expenses):
        console.print(Panel(f"[{insight.type.upper()}] {insight.message}", title=insight.title, border_style="blue"))
    console.print(Panel(ai_categorizer.generate_ai_summary(expenses), title="🤖 AI Summary", border_style="green"))

@app.command()
def clear():
    """Delete all expenses (confirmation required)."""
    if typer.confirm("⚠️  This will delete ALL expenses. Continue?"):
        import os
        if os.path.exists(storage.DB_PATH):
            os.remove(storage.DB_PATH)
        console.print("🗑️  Database cleared.")
    else:
        console.print("❌ Cancelled.")

if __name__ == "__main__":
    app()