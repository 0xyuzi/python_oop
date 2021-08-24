"""
https://www.youtube.com/watch?v=ZDa-Z5JzLYM

class: blueprint for creating instance 

"""
class Employee:
    pay = 500

    def __init__(self, first, last):
        self.first = first 
        self.last = last 
    
    def fullname(self):
        return f"{self.first}, {self.last}"
        

emp1 = Employee("Tao","He")
print(emp1.fullname())

print(Employee.fullname(emp1))

print(emp1.pay)
emp1.pay = 100
print(emp1.pay)
print(Employee.pay)