from Payment import payment

class Creditcard(payment):
    number = int
    CVV = int
    date = int
    def __init__(self,id,number,CVV,date):
        super().__init__(id)
        self.number = number
        self.CVV = CVV
        self.date = date