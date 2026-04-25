from datetime import date

expenses = []
# print total

# print each item

# print only > 2200

def show_summary(expenses):
    total = sum(expense["Amount"] for expense in expenses)
    max_expense = max(expense["Amount"] for expense in expenses)
    min_expense = min(expense["Amount"] for expense in expenses)

    print("Summary:")
    print(f"Total Expenses: {total}")
    print(f"Maximum Expense: {max_expense}")
    print(f"Minimum Expense: {min_expense}")

def add_expense(expenses):
    amount = int(input("Enter the amount: "))
    category = input("Enter the category: ")
    time = date.today()
    expenses.append({"Amount": amount, "Category": category, "Date": time})
    
    

while True:  
   add_expense(expenses)
   add_more = input("Do you want to add more expenses? Press 1 for Yes and 0 for No:  ")
   if add_more == "1":
       add_expense(expenses)
   elif add_more == "0":
       break
   else:
       print("Invalid input. Please enter 1 for Yes and 0 for No.")
       

want_summary = int(input("Do You want to see the summary? Enter 1 for Yes and 0 for No: "))
if want_summary ==1:
    show_summary(expenses)
elif want_summary == 0:
    print("Summary not displayed.")
else:
    print("Invalid input. Summary not displayed.")
   
