class Person:
    def __init__(self, name, age):
        self.name= name
        self.age=age

    def display_info(self):
        return (self.name, self.age)


class Member(Person):
    def __init__(self, member_id, borrowed_books):
        self.member_id = member_id
        self.borrowed_books = borrowed_books
    
    def borrow_book():
        pass
    def return_book():
        pass
    def display_info(): # (Override)
        pass

class Book:
    def __init__(self, title, author, isbn, available):
        self.title= title
        self.author = author
        self.isbn = isbn
        self.available = available

    def display_book():
        pass
    # Use encapsulation for available.
    # Create
    # Getter
    # Setter


class Library:
    def __init__(self,books, members):
        self.books = books
        self.members = members

    def add_book():
        pass
    def register_member():
        pass
    def borrow_book():
        pass
    def return_book():
        pass
    def show_books():
        pass
    def show_members():
        pass
    def search_book():
        pass

# Create an instance
person1 = Person("Alice", 30)

# Call the method
name, age = person1.display_info()
print(name)  # Output: Alice
print(age) 
def main():
    print("\n===================================================")
    print("========== ➡️ LIBRARY MANAGEMENT SYSTEM ⬅️ ==========")
    print("===================================================\n")
    print("# 1. Add Book")
    print("# 2. Register Member")
    print("# 3. Borrow Book")
    print("# 4. Return Book")
    print("# 5. Show All Books")
    print("# 6. Show All Members")
    print("# 7. Search Book")
    print("# 8. Exit")
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