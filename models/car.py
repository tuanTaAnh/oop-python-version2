
class Car:
    def __init__(self, serialnum, make, model, color, year, price):
        self.serialnum = serialnum
        self.make = make
        self.model = model
        self.color = color
        self.year = year
        self.price = price


    # getter method
    def get_invoiceID(self):
        return self.invoiceID

    # getter method
    def get_carID(self):
        return self.carID

    # getter method
    def get_salepersonID(self):
        return self.salepersonID

    # getter method
    def get_customerID(self):
        return self.customerID

    # getter method
    def get_year(self):
        return self.year

    # getter method
    def get_price(self):
        return self.price


    # setter method
    def set_serialnum(self, serialnum):
        self.serialnum = serialnum

    # setter method
    def set_make(self, make):
        self.make = make

    # setter method
    def set_model(self, model):
        self.salepersonID = model

    # setter method
    def set_color(self, color):
        self.color = color

    # setter method
    def set_year(self, year):
        self.year = year

    # setter method
    def set_price(self, price):
        self.price = price


    def get_infor(self):
        return self.serialnum + "," + self.make + "," + self.model + "," + self.color + "," + self.year + + "," + str(self.price) + "."