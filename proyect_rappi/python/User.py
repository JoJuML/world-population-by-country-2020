from email.headerregistry import Address
from Account import Account

class User(Account):
    address = str
    def __init__(self, name, document, address):
        super().__init__(name,document)
        self.address = address
