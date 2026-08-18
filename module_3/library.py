from book import Book
from member import Member
class Library:
    def __init__(self):
        self.books = []      
        self.members = [] 

# - - - - - - > ADD BOOK < - - - - - - #
    def add_book(self,title, author, isbn):
        for book in self.books:
            if book.isbn == isbn:
                raise ValueError(f"💥 The Entered ISBN '{isbn}' has already been added to the System. 💥")
        
        new_book = Book(title, author, isbn)
        self.books.append(new_book)
        print("Book 📖 added successfully! ✅")  

# - - - - - - > ADD MEMBER < - - - - - - #
    def register_member(self, name, age):
        new_member = Member( name, age)
        self.members.append(new_member)
        print("Member 🙂 added successfully! ✅")

# - - - - - - > BORROW BOOK < - - - - - - #
    def borrow_book(self, member_id, searched_book):
        member_exists = self.search_member(member_id)
        book_exists = self.search_book(searched_book)
        if book_exists.available == 'available':
            member_exists.borrow_book(book_exists.title)
            book_exists.available = 'borrowed'
            print(f"📖 Book {book_exists.title} has been added to the member {member_exists.member_id} - {member_exists.name} successfully. ✅")
        else: 
            raise ValueError("book 📖 is currently not available.❌ \nPlease check again later.")

# - - - - - - > RETURN BOOK < - - - - - - #
    def return_book(self, member_id, searched_book):
        member_exists = self.search_member(member_id)
        book_exists = self.search_book(searched_book)

        if searched_book in member_exists.borrowed_books and book_exists.available == 'borrowed':
            member_exists.return_book(book_exists.title)
            book_exists.available = 'available'
            print(f"📖 Book '{book_exists.title}' has been removed from the member '{member_exists.member_id} - {member_exists.name}' successfully. ✅")
            print("book 📖 returned.  ✅")
        else: 
            raise ValueError("The book 📖 has not borrowed yet by you.❌")
        
# - - - - - - > LIST ALL BOOKS < - - - - - - #
    def show_books(self):
        if not self.books:
            raise ValueError("No books 📖 in library. ❌")
        else:
            print("\n========== ➡️ BOOK LIST ⬅️ ==========\n")
            for book in self.books:
                print(book.display_book())

# - - - - - - > LIST ALL MEMBERS < - - - - - - #  
    def show_members(self):
        if not self.members:
            raise ValueError("No Member 🙂 in library. ❌")
        else:
            print("\n========== ➡️ MEMBER LIST ⬅️ ==========\n")
            for member in self.members:
                print(member.display_info()) 

# - - - - - - > SEARCH BOOK < - - - - - - #
    def search_book(self, searched_book):    
        if not self.books:
            raise ValueError("No books 📖 in library. ❌")
        else:
            for book in self.books:
                if(book.title == searched_book):
                    print(book.display_book())
                    return book
        raise ValueError(" No book with searched query found. 💥")

# - - - - - - > SEARCH MEMBER < - - - - - - #
    def search_member(self, searched_member):
        if not self.members:
            raise ValueError("No Members 🙂 in library.❌ \nAdd members to the Library System.")
        else:
            for member in self.members:
                if(member.member_id == searched_member):
                    print(member.display_info())
                    return member
                    
        raise ValueError("💥 No member with searched ID found. 💥")