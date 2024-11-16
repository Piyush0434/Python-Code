class Employee:
    language ="Py"  #This a class attribute
    salary = 1000000

emp = Employee()
emp.name="piyush"  #This is a instance attribute(object attribute)
print(emp.name,emp.salary,emp.language)
emp2 = Employee
emp2.name="Atharv"
print(emp2.name,emp2.salary,emp.language)

#Here name is object attribute & salary and language are 
# class atribute as they belong to the class