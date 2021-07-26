
class Invoice:
    def __init__(self, invoiceID, car, saleperson, customer, date):
        self.invoiceID = invoiceID
        self.carID = car.carID
        self.salepersonID = saleperson.salepersonID
        self.customerID = customer.customerID
        self.date = date


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
    def get_date(self):
        return self.date

    # setter method
    def set_invoiceID(self, invoiceID):
        self.invoiceID = invoiceID

    # setter method
    def set_carID(self, carID):
        self.carID = carID

    # setter method
    def set_salepersonID(self, salepersonID):
        self.salepersonID = salepersonID

    # setter method
    def set_customerID(self, customerID):
        self.customerID = customerID

    # setter method
    def set_date(self, date):
        self.date = date


    def get_infor(self):
        return self.invoiceID + "," + self.carID + "," + self.salepersonID + "," + self.customerID + "," + self.date + "."