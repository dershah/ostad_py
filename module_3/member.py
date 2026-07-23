from person import Person
class Member(Person):
    def __init__(self,name, age, member_id, borrowed_books):
        super().__init__(name, age)
        self.member_id = member_id
        self.borrowed_books = borrowed_books
    
    def borrow_book():
        pass
    def return_book():
        pass
    def display_info(self): # (Override)
        return f"ID: {self.member_id}  Name: {self.name}  Age: {self.age}  Book: {self.borrowed_books}"