class Programmer:
    company="Microsoft"
    def __init__(self,name,salary,pin):
        self.name=name
        self.salary=salary
        self.pin=pin

p=Programmer("Piyush",1200000,421136)
print(p.name,p.salary,p.pin,p.company)
r=Programmer("Atharv",1200000,421136)
print(r.name,r.salary,r.pin,r.company)
