from random import randint

class Train():
    def book(self,trainNo,fro,to):
        print(f"Ticket is booked of trainNo : {trainNo} from {fro} to {to}")

    def getStatus (self,trainNo):
        print("Train no :{trainNo} is runnibg on time")

    def getFare(self,trainNo,fro,to):
        print(f"Ticket fare in trainNo :{trainNo} from {fro} to {to} is {randint(222,555)}")

t = Train()
t.book(4,"kop","Ayodhya")
t.getStatus(4)
t.getFare(4,"kop","Ayodhya")