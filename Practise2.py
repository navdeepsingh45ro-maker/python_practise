from datetime import date
import json

try:
    with open("expenses.json","r") as file:
        expenses = json.load(file)
except:
    expenses = []


def show_summary(expenses):
    total = sum(expense["Amount"] for expense in expenses)
    max_expense = max(expense["Amount"] for expense in expenses)
    min_expense = min(expense["Amount"] for expense in expenses)

    print("Summary:")
    print(f"Total Expenses: {total}")
    print(f"Maximum Expense: {max_expense}")
    print(f"Minimum Expense: {min_expense}")

def add_expense(expenses):
     while True:
        amount = int(input("Enter the amount: "))
        category = input("Enter the category: ")
        time = str(date.today())
        expenses.append({"Amount": amount, "Category": category, "Date": time})
        with open("expenses.json", "w") as file:
            json.dump(expenses, file)
        add_more = input("Do you want to add more expenses? Press 1 for Yes and 0 for No:  ")
        if add_more == "1":
            continue
        elif add_more == "0":
            break
        else:
            print("Invalid input. Please enter 1 for Yes and 0 for No.")  

def show_expenses(expenses):
    print("Expenses:")
    for expense in expenses:
        print(f"Amount: {expense['Amount']}, Category: {expense['Category']}, Date: {expense['Date']}")
        if not expenses:
          print("No expenses yet.")
        return 


print("Welcome to the Expense Tracker!")
menu = """1. Add an expense
2. View expenses
3. View summary
4. Exit
"""
print(menu)
while True: 
    choice = input("Please select an option (1-4): ")
    if choice == "1":
        add_expense(expenses)
    elif choice == "2":
        show_expenses(expenses)
    elif choice == "3":        
        show_summary(expenses)
    elif choice == "4":
     break
    else:
        print("Invalid choice. Please select a valid option (1-4).")


   
