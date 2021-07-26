
class ServiceDetail:
    def __init__(self, serdetID, serviceticket, service, mechanic, part, quan_of_part, total_price):
        self.serdetID = serdetID
        self.serticID = serviceticket.serticID
        self.serviceID = service.serviceID
        self.mechanicID = mechanic
        self.partID = part.partID
        self.quan_of_part = quan_of_part
        self.total_price = total_price


    # getter method
    def get_serdetID(self):
        return self.serdetID

    # getter method
    def get_serticID(self):
        return self.serticID

    # getter method
    def get_serviceID(self):
        return self.serviceID

    # getter method
    def get_mechanicID(self):
        return self.mechanicID

    # getter method
    def get_partID(self):
        return self.partID

    # getter method
    def get_quan_of_part(self):
        return self.quan_of_part

    # getter method
    def get_quan_of_part(self):
        return self.quan_of_part

    # getter method
    def get_total_price(self):
        return self.total_price

    # setter method
    def set_serdetID(self, serdetID):
        self.serdetID = serdetID

    # setter method
    def set_serticID(self, serviceticket):
        self.serticID = serviceticket.serticID

    # setter method
    def set_serviceID(self, service):
        self.serviceID = service.serviceID

    # setter method
    def set_mechanicID(self, mechanic):
        self.mechanicID = mechanic.mechanicID

    # setter method
    def set_partID(self, part):
        self.partID = part.partID

    # setter method
    def set_quan_of_part(self, quan_of_part):
        self.quan_of_part = quan_of_part

    # setter method
    def set_total_price(self, total_price):
        self.total_price = total_price


    def get_infor(self):
        return self.serdetID + "," + self.serticID + "," + self.serviceID + "," + self.mechanicID + "," + self.partID+ "," + str(self.quan_of_part) + "," + str(self.total_price) + "."