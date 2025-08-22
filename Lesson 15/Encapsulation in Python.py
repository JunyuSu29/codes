class Person:
    def __init__(self):
        self.__name="Student"
        self.__age=10
    
    def set_age(self,age):
        self.__age=age
        if age<0:
            raise ValueError("Age cannot be negative")

    def set_name(self,name):
        self.__name=name
        if not name:
            raise SyntaxError("Name cannot be empty")
    
    
    def get_name(self):
        return f"Name: {self.__name}"
    
    def get_age(self):
        return f"Age:{self.__age}"

person=Person()
print(person.get_name()) #Returns default name "Student"
person.set_name("John")
print(person.get_name()) #Returns updated name "John"
print(person.get_age()) #Returns default age 10
person.set_age(20)
print(person.get_age()) #Returns updated age 20
person.set_name("")
print(person.get_name()) #Raises SyntaxError
person.set_age(-1)
print(person.get_age()) #Raises ValueError