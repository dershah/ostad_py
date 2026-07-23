class Person:
    def __init__(self, name, age):
        self.name= name
        self.age=age

    def display_info(self):
        return (self.name, self.age)