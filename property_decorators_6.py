"""
https://www.youtube.com/watch?v=jCzT9XFZ5bw
setter, getter, deleters 

"""
class Employee:
    def __init__(self, first, last):
        self.first = first 
        self.last = last 
    @property
    def fullname(self):
        return f"{self.first}, {self.last}"
    @property 
    def email(self):
        return f"{self.first}.{self.last}@email.com"

    @fullname.setter
    def fullname(self,name):
        first, last = name.split(" ")
        self.first = first 
        self.last = last 
    
    @fullname.deleter
    def fullname(self):
        print("Delete Name!")
        self.first = None  
        self.last = None 


# example
emp1 = Employee("Tao", "He")
print(emp1.email)

emp1.fullname = "Tom He"
print(emp1.fullname)
print(emp1.email)
email = emp1.email 
print(f"assign email to {email}")

del emp1.fullname 

print(emp1.email)
