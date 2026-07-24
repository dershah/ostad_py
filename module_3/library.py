from book import Book
from member import Member
class Library:
    def __init__(self):
        self.books = []      
        self.members = [] 

    def add_book(self,title, author, isbn):
        new_book = Book(title, author, isbn)
        self.books.append(new_book)
        print("Book 📖 added successfully! ✅")
        print(self.books)

    def register_member(self,member_id, name, age,  borrowed_books):
        new_member = Member( name, age, member_id, borrowed_books)
        self.members.append(new_member)
        print("Member 🙂 added successfully! ✅")
        print(self.members)

    def borrow_book(self, searched_book):
        book_exists = self.search_book(searched_book)
        print(f"book: {book_exists}")

        self.books.remove(book_exists)
        print("book 📖 borrowed successfully. ✅")

    def return_book(self, searched_book):
        print("book 📖 returned.  ✅")

    def show_books(self):
        if not self.books:
            print("No books 📖 in library. ❌")
        else:
            for book in self.books:
                print(book.display_book())
            
    def show_members(self):
        if not self.members:
            print("No Member 🙂 in library. ❌")
        else:
            for member in self.members:
                print(member.display_info()) 

    def search_book(self, searched_book):
        found= False      
        if not self.books:
            print("No books 📖 in library. ❌")
        else:
            for book in self.books:
                if(book.title == searched_book):
                    print(book.display_book())
                    found= True
                    return book
            if(not found):
                print("No book with searched query found. 💥")