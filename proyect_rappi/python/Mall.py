from Products import Products

class Mall(Products):
    name_mall = str
    def __init__(self,name,brand,amount,name_mall):
        super().__init__(name,brand,amount)
        self.name_mall = name_mall