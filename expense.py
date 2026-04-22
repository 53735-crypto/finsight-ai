# each expense is a dictinary:{'category:'food','amount':500}
# and we use a global list to store data
expenses=[]
def add_expense():
    print("\n Add New Expense ")
    category = input("Enter Category (Food, Travel, etc.): ")

    amount = float(input("Enter Amount: "))
    expense_data = {
        'category': category,
        'amount': amount
    }
    expenses.append(expense_data)
    print("Expense added successfully!")



# we need afunction to calculate the total
def get_total_expenses():
    total = 0.0
    for item in expenses:
        total = total + item['amount']
    print(f"\nTotal Expenses: Rs.{total}")


# algorithm to find which expense was most expensive
def find_most_expensive():
    if len(expenses) == 0:
        print("No expenses to check.")
        return
    max_expense = expenses[0]
    
    
    for item in expenses:
        if item['amount'] > max_expense['amount']:
            max_expense = item
    print(f"\nMost Expensive Purchase: {max_expense['category']} - ₹{max_expense['amount']}")


# to show latest added input we use reversal alogrithm
def view_history_reversed():
    print("\n Expense History (Newest First)")
    n = len(expenses)
    for i in range(n - 1, -1, -1):
        item = expenses[i]
        print(f"{i + 1}. {item['category']}: Rs.{item['amount']}")

# now tie all together with infinite loop
def main_menu():
    while True:
            print("\nEXPENSE MANAGER BY SUSHANT KUMAR")
            print("1. Add Expense")
            print("2. View History (Reversed)")
            print("3. Calculate Total (Summation)")
            print("4. Find Max Expense (Max Algorithm)")
            print("5. Exit")

            choice = input("Enter choice (1-5): ")
            
            # Topic: Conditionals (if-elif-else)
            if choice == '1':
                add_expense()
            elif choice == '2':
                view_history_reversed()
            elif choice == '3':
                get_total_expenses()
            elif choice == '4':
                find_most_expensive()
            elif choice == '5':
                print("Exiting program...")
                break
            else:
                print("Invalid choice, try again.")
main_menu()