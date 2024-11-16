class Employee:
    company ="ITC"

    def __init__(self,name,salary,language):
        self.name=name
        self.salary=salary
        self.language=language
    
    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary}")

# class Programmer:
#     company="ITC Infotech"
#     def show(self):
#         print(f"The name is {self.name} and the salary is{self.salary}")

#     def showLang(self):
#         print(f"The name is {self.name} and he is good with {self.language} language")

class Programmer(Employee):
     company ="ITC Infotech"
     def showLang(self):
        print(f"The name is {self.name} and he is good with {self.language} language")

a=Employee("piyush",50000000,"JavaScript")
b=Programmer("Piyush",50000000,"Python")

b.show()
b.showLang()
