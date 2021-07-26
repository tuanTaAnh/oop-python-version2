
class Mechanic:
    def __init__(self, mechanicID, lastname, firstname, birthdate):
        self.mechanicID = mechanicID
        self.lastname = lastname
        self.firstname = firstname
        self.birthdate = birthdate


    # getter method
    def get_mechanicID(self):
        return self.mechanicID

    # getter method
    def get_lastname(self):
        return self.lastname

    # getter method
    def get_firstname(self):
        return self.firstname

    # getter method
    def get_birthdate(self):
        return self.birthdate

    # setter method
    def set_mechanicID(self, mechanicID):
        self.mechanicID = mechanicID

    # setter method
    def set_lastname(self, lastname):
        self.lastname = lastname

    # setter method
    def set_firstname(self, firstname):
        self.firstname = firstname

    # setter method
    def set_birthdate(self, birthdate):
        self.birthdate = birthdate


    def __str__(self):
        return self.mechanicID + "," + self.lastname + "," + self.firstname + "," + self.birthdate + "."