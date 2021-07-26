
class Service:
    def __init__(self, serviceID, typ, price):
        self.serviceID = serviceID
        self.typ = typ
        self.price = price


    # getter method
    def get_serviceID(self):
        return self.serviceID

    # getter method
    def get_typ(self):
        return self.typ

    # getter method
    def get_price(self):
        return self.price


    # setter method
    def set_serviceID(self, serviceID):
        self.serviceID = serviceID

    # setter method
    def set_typ(self, typ):
        self.typ = typ

    # setter method
    def set_price(self, price):
        self.price = price


    def __str__(self):
        return self.serviceID + "," + self.typ + "," + str(self.price) + "."