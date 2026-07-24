import sys
from library import Library
from book import Book
from member import Member

# Create an instance
# member1 = Member("Alice", 30)
member1 = Member("Alice",30,1,"Python Programming")
print(member1.display_info())

# Call the method
# name, age = person1.display_info()
# print(name)  # Output: Alice
# print(age) 
def display_menu():
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

def main():

 
    libary = Library()
    while True:
        try:
            display_menu()
            choice= int(input("Enter An Option: "))
            if choice==1:
                title= input("Enter Title: ")
                Author= input("Enter Author: ")
                isbn = input("Enter ISBN: ")
                libary.add_book(title, Author, isbn)
            elif choice==2:
                id = int(input("Enter user ID: "))
                name = input("Enter User name: ").strip()
                age = int(input("Enter User Age: "))
                book_name= input("Enter Book Name: ").strip()
                libary.register_member(id, name, age, book_name)
                
            elif choice==3:
                searched_book= input("What book are you looking borrow 👀:")
                libary.borrow_book(searched_book)
            elif choice==4:
                searched_book= input("What book are you looking borrow 👀:")
                libary.return_book(searched_book)
            elif choice==5:
                libary.show_books()
            elif choice==6:
                libary.show_members()
            elif choice==7:
                searched_book= input("What book are you searching 👀:")
                libary.search_book(searched_book)
            elif choice==8:
                print("\n########## - The App ended by the choice of user ✅ - ##########\n")
                sys.exit(0)
            else:
                raise ValueError("Invalid Menu Option")

        except Exception as error:
            print(f"\n########## - 💥{error}💥 - ##########\n")

if __name__ == "__main__":
    main()