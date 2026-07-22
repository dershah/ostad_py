import os

FILE_NAME = "expenses.txt"

# ========= Read File =========


def read_expenses():
    expenses=[]
    if not os.path.exists(FILE_NAME):
        raise FileNotFoundError(f"\n########## - ❌No expense records found.❌ - ##########\n")
    with open(FILE_NAME, 'r') as file:
        lines = file.readlines()
    if not lines:
        raise ValueError(f"\n########## - ❌No expenses available.❌ - ##########\n")

    for line in lines:
        line=line.strip()
        parts = line.split(',')

        expense ={
            'id': parts[0].strip(),
            'date': parts[1].strip(),
            'category': parts[2].strip(),
            'description': parts[3].strip(),
            'amount': parts[4].strip()
        }
        expenses.append(expense)
    return expenses

# ========= Write File =========     

def write_expenses(expenses):
    """Write list of expenses to file."""
    with open(FILE_NAME, 'w') as f:
        for exp in expenses:
            f.write(f"{exp['id']},{exp['date']},{exp['category']},{exp['description']},{exp['amount']}\n")

# 1. Add Expense ========= ========= ========= ========= 
        
def add_expense():        
    try:
        exp_id= int(input("Entery Number: "))
        date= input("Enter Date (YYYY-MM-DD): ")  
        category= input("Enter Category: ")  
        description= input("Enter Description: ")  
        amount= int(input("Enter Amount: "))
    except ValueError:
        print("Invalid amount! Please enter a valid number.")
        return
    if amount < 0:
        print("Amount cannot be negative.")
        return
    try:
        expenses = read_expenses()
    except (FileNotFoundError, ValueError):
        expenses = []

    for exp in expenses:
        if exp_id == int(exp['id']):
            print(f"Expense ID - {exp_id} already exists. Please use a unique ID.")
            return
    new_exp = {
           'id': exp_id,
            'date': date,
            'category': category,
            'description': description,
            'amount': amount
        }
        
    expenses.append(new_exp)
    write_expenses(expenses)
    print("\n########## - A New Expense Added Successfully 😀 - ##########\n")
    main()


# 2. View All Expenses ========= ========= ========= =========

def view_expenses():
    for expense in read_expenses():
        print("------------------------------------\n")
        print(f"Expense ID : {expense["id"]}")
        print(f"Date : {expense["date"]}")
        print(f"Category : {expense["category"]}")
        print(f"Description : {expense["description"]}")
        print(f"Amount : {expense["amount"]}")

    main()

# 3. Search Expense ========= ========= ========= =========


def search_expense():
    searched_id= input("Enter the Expense ID, you are looking for 🔎: ")
    expense_found=False
    for expense in read_expenses():
        if expense['id'] == searched_id:
            print("\n########## - ✅Expense Found✅ - ##########\n")
            print(f"Expense ID : {expense["id"]}")
            print(f"Date : {expense["date"]}")
            print(f"Category : {expense["category"]}")
            print(f"Description : {expense["description"]}")
            print(f"Amount : {expense["amount"]}")
            expense_found=True
    if not expense_found:
        print(f"\n########## - ❌Expense not found.❌ - ##########\n")

    main()    

# 4. Update Expense ========= ========= ========= =========

def update_expense():
    expenses=[]
    searched_id= input("Enter the Expense ID, you want to Update ⬆️: ")
    expense_found=False
    for expense in read_expenses():
        if expense['id'] == searched_id:
            print("\n########## - Expense Found - ##########\n")
            try:         
                date= input("Enter Date (YYYY-MM-DD): ")  
                category= input("Enter Category: ")  
                description= input("Enter Description: ")  
                amount= int(input("Enter Amount: "))
                update_exp={
                    'id':expense['id'],
                    'date': date,
                    'category': category,  
                    'description': description,  
                    'amount': amount,
                }
            except ValueError:
                print("Invalid amount! Please enter a valid number.")
                return
            if amount < 0:
                print("Amount cannot be negative.")
                return
            expense_found=True
            expenses.append(update_exp)
            print("\n########## - Expense upated Successfully✅ - ##########\n")
        else:
            expenses.append(expense)
    write_expenses(expenses)
    if not expense_found:
        print(f"\n########## - ❌Expense not found.❌ - ##########\n")

    main()

# 5. Delete Expense  ========= ========= ========= =========

def delete_expense():
    expenses=[]
    searched_id= input("Enter the Expense ID, you want to delete 🗑️: ")
    expense_found=False
    list= read_expenses()
    for expense in list:
        if expense['id'] == searched_id:
            print("\n########## - Expense Found - ##########\n")
            list.remove(expense)
            expense_found=True
        
            print("\n########## - Expense Deleted Successfully✅ - ##########\n")

    write_expenses(list)
    if not expense_found:
        print(f"\n########## - ❌Expense not found.❌ - ##########\n")

    main()

# 6. Expense Summary  ========= ========= ========= =========

def expense_summary():
    all_expenses_amount=[]
    number_of_expenses=0

    for expense in read_expenses():
        all_expenses_amount.append(int(expense['amount']))
        number_of_expenses+=1
    Total_amount=sum(all_expenses_amount) 

    average_amount= round(Total_amount/number_of_expenses)
    highest_expense= max(all_expenses_amount)
    lowest_expense= min(all_expenses_amount)

    print(f"\nTotal Expenses  : {number_of_expenses}")
    print(f"\nTotal Spending  : {Total_amount} BDT")
    print(f"\nAverage Expense : {average_amount} BDT")
    print(f"\nHighest Expense : {highest_expense} BDT")
    print(f"\nLowest Expense  : {lowest_expense} BDT\n")

    main()

# Main function ========= ========= ========= =========

def main():
    print("\n\n========= ➡️ Expense Tracker ⬅️ =========\n")
    print("# 1. Add Expense")
    print("# 2. View All Expenses")
    print("# 3. Search Expense")
    print("# 4. Update Expense")
    print("# 5. Delete Expense")
    print("# 6. Expense Summary")
    print("# 7. Exit")
    try:
        choice= int(input("Enter An Option: "))
        if choice==1:
            add_expense()
        elif choice==2:
            view_expenses()
        elif choice==3:
            search_expense()
        elif choice==4:
            update_expense()
        elif choice==5:
            delete_expense()
        elif choice==6:
            expense_summary()
        elif choice==7:
            print("\n########## - The App ended by the choice of user ✅ - ##########\n")
        else:
            raise ValueError("Invalid Menu Option")

    except Exception as error:
        print(f"\n########## - ❌{error}❌ - ##########\n")

if __name__ == "__main__":
    main()