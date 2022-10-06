from User import User
from Deliver import Deliver
from Route import Route
from Payment import Payment
from Products import Products

class Delivering:
    id = int
    User = User("","","")
    product = Products("","","")
    deliver = Deliver("","")
    route = Route
    payment = Payment
    def __init__(self,user,product,deliver,payment):
        self.user = user
        self.product = product
        self.deliver = deliver
        self.payment = payment