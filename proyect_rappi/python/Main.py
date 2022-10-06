from Products import Products
from Mall import Mall
from Delivering import Delivering
from User import User
from Deliver import Deliver
from Payment import Payment

if __name__ =='__main__':
    prod2 = Products("helado","la michoacana",3)
    print(vars(prod2))
    newprod = Mall("mayonesa","makcornic",2,"soriana")
    print(vars(newprod))
    entrega1 = Delivering(User("deyanira herrera","BASIC","..."),Products("helado","la michoacana",3),Deliver("jesus marquez","DEL"),Payment(876659))
    print(vars(entrega1))