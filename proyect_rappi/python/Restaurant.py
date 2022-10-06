from Products import Products

class Restaurant(Products):
    type_food = str
    sell_by_date = str
    name_rest = str
    def __init__(self,name,brand,amount,type_food,sell_by_date,name_rest):
        super().__init__(name,brand,amount)
        self.type_food = type_food
        self.sell_by_date = sell_by_date
        self.name_rest = name_rest
