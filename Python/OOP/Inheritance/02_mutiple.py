# class Mother:
#     mothername = ""
 
#     def mother(self):
#         print(self.mothername)
 
 
# class Father:
#     fathername = ""
 
#     def father(self):
#         print(self.fathername)
 
 
# class Son(Mother, Father):
#     def parents(self):
#         print("Father name is :", self.fathername)
#         print("Mother :", self.mothername)
# s1 = Son()
# s1.fathername = "Virat"
# s1.mothername = "Anushka"
# s1.parents()

class Employee:
    company ="ITC"

    name="piyush"
    def show(self):
        print(f"The name of employee is {self.name} and the company is {self.company}")
class Coder:
    language="Python"
    def printLang(self):
        print(f"Out of all languages here is your language : {self.language}")

class Programmer(Employee,Coder):
     company ="ITC Infotech"
     def showLang(self):
        print(f"The name is {self.company} and he is good with {self.language} language")

a=Employee()
b=Programmer()

print(b.company,a.company)
b.show()
b.printLang()
b.showLang()
