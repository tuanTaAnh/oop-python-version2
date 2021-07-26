
class Part:
    def __init__(self, partID, name, description, price):
        self.partID = partID
        self.name = name
        self.description = description
        self.price = price


    # getter method
    def get_partID(self):
        return self.partID

    # getter method
    def get_name(self):
        return self.name

    # getter method
    def get_description(self):
        return self.description

    # getter method
    def get_price(self):
        return self.price

    # setter method
    def set_partID(self, partID):
        self.partID = partID

    # setter method
    def set_name(self, name):
        self.name = name

    # setter method
    def set_description(self, description):
        self.description = description

    # setter method
    def set_price(self, price):
        self.price = price


    def __str__(self):
        return self.partID + "," + self.name + "," + self.description + "," + str(self.price) + "."