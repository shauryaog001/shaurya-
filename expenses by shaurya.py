import json
import datetime
import os

DATA_FILE = "data.json"

def load_data():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as file:
        return json.load(file)

def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

def add_expense():
    print("\n--- Add Expense ---")
    title = input("Enter expense title: ")
    amount = float(input("Enter amount: "))
    date = str(datetime.date.today())

    expense = {
        "title": title,
        "amount": amount,
        "date": date
    }

    data = load_data()
    data.append(expense)
    save_data(data)
    print("Expense added successfully!")

def view_expenses():
    print("\n--- All Expenses ---")
    data = load_data()
    
    if not data:
        print("No expenses recorded yet.")
        return
    
    for i, exp in enumerate(data, 1):
        print(f"{i}. {exp['title']} - ₹{exp['amount']} on {exp['date']}")

def delete_expense():
    print("\n--- Delete Expense ---")
    data = load_data()
    
    if not data:
        print("No expenses to delete.")
        return
    
    view_expenses()
    idx = int(input("Enter the number to delete: "))
    
    if 1 <= idx <= len(data):
        removed = data.pop(idx - 1)
        save_data(data)
        print(f"Deleted: {removed['title']} (₹{removed['amount']})")
    else:
        print("Invalid index.")

def monthly_report():
    print("\n--- Monthly Report ---")
    data = load_data()
    if not data:
        print("No data available.")
        return
    
    month = input("Enter month (MM): ")
    year = input("Enter year (YYYY): ")

    total = 0
    print(f"\nExpenses for {month}/{year}:")

    for exp in data:
        exp_date = datetime.datetime.strptime(exp["date"], "%Y-%m-%d")
        if exp_date.month == int(month) and exp_date.year == int(year):
            print(f"- {exp['title']}: ₹{exp['amount']}")
            total += exp["amount"]

    print(f"\nTotal Spent = ₹{total}")

def main():
    while True:
        print("\n===== Expense Tracker =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Monthly Report")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            delete_expense()
        elif choice == "4":
            monthly_report()
        elif choice == "5":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
