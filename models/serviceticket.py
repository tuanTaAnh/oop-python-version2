
class ServiceTicket:
    def __init__(self, serticID, car, customer, datein, dateout, status, totalcost):
        self.serticID = serticID
        self.carID = car.serialnum
        self.customerID = customer.customerID
        self.datein = datein
        self.dateout = dateout
        self.status = status
        self.totalcost = totalcost


    # getter method
    def get_serticID(self):
        return self.serticID

    # getter method
    def get_carID(self):
        return self.carID

    # getter method
    def get_customerID(self):
        return self.customerID

    # getter method
    def get_datein(self):
        return self.datein

    # getter method
    def get_dateout(self):
        return self.dateout

    # getter method
    def get_status(self):
        return self.status

    # getter method
    def get_totalcost(self):
        return self.totalcost

    # setter method
    def set_serticID(self, serticID):
        self.serticID = serticID

    # setter method
    def set_carID(self, car):
        self.carID = car.carID

    # setter method
    def set_customerID(self, customer):
        self.customerID = customer.customerID

    # setter method
    def set_datein(self, datein):
        self.datein = datein

    # setter method
    def set_dateout(self, dateout):
        self.dateout = dateout

    # setter method
    def set_status(self, status):
        self.status = status

    # setter method
    def set_totalcost(self, totalcost):
        self.totalcost = totalcost


    def __str__(self):
        return self.serticID + "," + self.carID + "," + self.customerID + "," + self.datein + "," + self.dateout+ "," + self.status+ "," + str(self.totalcost) + "."