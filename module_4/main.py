import sys
from library import Library
from book import Book
from member import Member

# Create an instance
# member1 = Member("Alice", 30)
member1 = Member("Alice",30,1,"Python Programming")
print(member1.display_info())


def display_menu():
    print("\n===================================================================")
    print("========== ➡️ Real-Time Weather & Currency Data Fetcher ⬅️ ==========")
    print("===================================================================\n")
    print("# 1. Current Weather")
    print("# 2. Currency Exchange Rate")
    print("# 3. Save Result to JSON File")
    print("# 4. View Previous Saved Data")
    print("# 8. Exit")

def main():
    libary = Library()
    while True:
        try:
            display_menu()
            choice= int(input("Enter An Option: "))
            if choice==1:
                pass
            elif choice==2:
                pass
                
            elif choice==3:
                pass
            elif choice==4:
                pass
            elif choice==5:
                print("\n########## - The App ended by the choice of user ✅ - ##########\n")
                sys.exit(0)
            else:
                raise ValueError("Invalid Menu Option")

        except Exception as error:
            print(f"\n########## - 💥{error}💥 - ##########\n")

if __name__ == "__main__":
    main()