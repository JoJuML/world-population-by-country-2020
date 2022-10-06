from Products import products

class drugstore(products):
    expiration = int # the expiration date
    name_drug =str
    def __init__(self,name,brand,expiration,name_drug):
        super().__init__(name,brand)
        self.expiration = expiration
        self.name_drug = name_drug