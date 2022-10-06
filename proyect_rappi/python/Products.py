class Products:
    id = int
    name = str
    cost = float
    brand = str
    amount = int
    type = str
    
    def __init__(self,name,brand,amount):
        self.name = name
        self.brand = brand
        self.amount = amount