class Employee:
    a=1

    @classmethod    #it helps in showing class attribute instead of instance attribute
    def show(cls):
        print(f"The value of a is : {cls.a}")

e=Employee()
e.a=45
e.show()