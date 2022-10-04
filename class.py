def __init__(self, name, address):
    self.name = name
    self.address = address
    
class Person:
    name = 'No name provided'
    address = ' '
 
class Student(Person):
    GPA = 3.8
    Grade = 8

class Teacher(Person):
    Department = 'Physical Education'
    Salary = 35,000
    
    
