from Products import Products

class store(Products):
    name_store = str
    def __init__(self,name,brand,name_store):
        super().__init__(name,brand)
        self.name_store = name_store