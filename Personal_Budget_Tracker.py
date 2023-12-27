import json
import os

def load_data():
    if os.path.exists('budget_data.json'):
        with open('budget_data.json', 'r') as file:
            return json.load(file)
    else:
        return {'income': 0, 'expenses': []}

def save_data(data):
    with open('budget_data.json', 'w') as file:
        json.dump(data, file)

def display_menu():
    print("\n===== Budget Tracker Menu =====")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Budget")
    print("4. View Expense Analysis")
    print("5. Exit")

def add_income(data):
    amount = float(input("Enter income amount: "))
    data['income'] += amount
    print(f"Income of ${amount} added successfully!")

def add_expense(data):
    category = input("Enter expense category: ")
    amount = float(input("Enter expense amount: "))
    data['expenses'].append({'category': category, 'amount': amount})
    print(f"Expense of ${amount} under '{category}' added successfully!")

def view_budget(data):
    remaining_budget = data['income'] - sum(expense['amount'] for expense in data['expenses'])
    print(f"\nIncome: ${data['income']:.2f}")
    print(f"Expenses: ${sum(expense['amount'] for expense in data['expenses']):.2f}")
    print(f"Remaining Budget: ${remaining_budget:.2f}")

def view_expense_analysis(data):
    categories = set(expense['category'] for expense in data['expenses'])
    print("\n===== Expense Analysis =====")
    for category in categories:
        category_expenses = [expense['amount'] for expense in data['expenses'] if expense['category'] == category]
        total_expenses = sum(category_expenses)
        print(f"{category}: ${total_expenses:.2f}")

def main():
    data = load_data()

    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            add_income(data)
        elif choice == '2':
            add_expense(data)
        elif choice == '3':
            view_budget(data)
        elif choice == '4':
            view_expense_analysis(data)
        elif choice == '5':
            save_data(data)
            print("Budget data saved. Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
