class Calculator:

    def __init__(self,a):
        self.a=a

    def square(self):
        print(self.a*self.a)
    
    def cube(self):
        print(self.a*self.a*self.a)
    
    def sqrroot(self):
        print(self.a**1/2)
    
    @staticmethod
    def greet():
        print("Hello")

n=Calculator(4)
n.square()
n.cube()
n.sqrroot()
n.greet()
