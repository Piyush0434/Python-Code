class Employee:
    language="Python"
    salary= 1200000

    def getInfo(self):
        print(f"The laguage is {self.language}.The salary is {self.salary}")

    # def greet(self):
    #     print("Good morning")

    @staticmethod
    def greet():
        print("Good morning")

emp = Employee()
emp.language="JavaScript"
# print(emp.salary,emp.language)
emp.getInfo()
emp.greet()
