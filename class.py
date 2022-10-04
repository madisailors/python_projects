def __init__(self, name, address):
    self.name = name
    self.address = address
    
class Person: #All child classes will have name and address attributes
    name = 'No name provided'
    address = ' '
 
class Student(Person): #Child class of Person, adding unique attributes
    GPA = 3.8
    Grade = 8

class Teacher(Person):
    Department = 'Physical Education'
    Salary = 35,000
    
    
