from person import Person
class Member(Person):
    cls_id=1
    def __init__(self,name, age):
        super().__init__(name, age)
        self.member_id = f"L-{Member.cls_id}"
        Member.cls_id+=1
        self.borrowed_books=[]
    
    def borrow_book(self, borrowed_book):
        self.borrowed_books.append(borrowed_book)

    def return_book(self, returned_book):
        self.borrowed_books.remove(returned_book)
        
    def display_info(self): # (Override)
        return f"|- ID: {self.member_id} -|- Name: {self.name} -|- Age: {self.age} -|- Book: {self.borrowed_books}\n"