import email
from Payment import payment

class Paypal(payment):
    email = str
    def __init__(self,id,email):
        super().__init__(id)
        self.email = email
    