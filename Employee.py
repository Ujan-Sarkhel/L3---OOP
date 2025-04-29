class Person:
    def __init__(self, name, idnumber):
        self.name=name
        self.idnumber=idnumber
    def display(self):
        print(self.name)
        print(self.idnumber)
class Employee:
    def __init__(self, name, idnumber, salary, post):
        self.salary=salary
        self.post=post
        Person.__init__(self, name, idnumber)
ob=Employee("Rahul", "e3242","325231 lpa","Assistant Sales Manager")
print("Name:", ob.name,'\n''Id number:',ob.idnumber,'\n''Salary:',ob.salary,'\n''Post:',ob.post)
        