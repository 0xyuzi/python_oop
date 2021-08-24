"""
https://www.youtube.com/watch?v=BJ-VvGyQxho&t=0s

class variables 
share among 
"""

class Employee:
    num_emps = 0
    raise_amount = 1.04 
    
    def __init__(self, first, last, pay):
        self.first = first 
        self.last = last 
        self.pay = pay 
        Employee.num_emps += 1 

    def fullname(self):
        return f"{self.first}, {self.last}"

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

print(Employee.num_emps)
emp1 = Employee("Tao", "He", 20000)
print(emp1.raise_amount)
print(Employee.raise_amount)

# print(emp1.__dict__)
# print(Employee.__dict__)

Employee.raise_amount = 1.05 
print(emp1.raise_amount)
print(Employee.raise_amount)

emp1.raise_amount = 1.10

print(emp1.raise_amount)
print(Employee.raise_amount)
# print(emp1.__dict__)

emp2 = Employee("Tom", "He", 20000)
print(Employee.num_emps)
print(emp1.num_emps)
print(emp2.num_emps)