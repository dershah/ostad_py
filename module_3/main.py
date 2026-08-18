import sys
from library import Library
from book import Book
from member import Member

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
            choice= int(input("\n\n➡️  Enter An Option: "))
            if choice==1:
                title= input("Enter Title: ").strip().lower()
                author= input("Enter Author: ").strip().lower()
                isbn = input("Enter ISBN: ").strip()
                if not title or not author or not isbn:
                    raise ValueError("Title, Author, and ISBN cannot be empty.")
                libary.add_book(title, author, isbn)
            elif choice==2:
                # id = input("Enter user ID [L-X]: ")
                name = input("Enter User name: ").strip().lower()
                age = input("Enter User Age: ").strip()

                if not name or not age:
                    raise ValueError("Name and Age cannot be empty.")
                int_age= int(age)
                if int_age <= 0:
                    raise ValueError("Error: Age must be greater than 0")
                libary.register_member( name, int_age)
                
            elif choice==3:
                member_id= input("Member ID [L-X]:")
                searched_book= input("What book are you looking borrow:").strip().lower()
                libary.borrow_book(member_id, searched_book)
            elif choice==4:
                member_id= input("Member ID [L-X]:")
                searched_book= input("What book are you returning:").strip().lower()
                libary.return_book(member_id, searched_book)
            elif choice==5:
                libary.show_books()
            elif choice==6:
                libary.show_members()
            elif choice==7:
                searched_book= input("What book are you searching 👀:").strip().lower()
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