
class SalePerson:
    def __init__(self, salemanID, firstname, lastname, gender, photo):
        self.salemanID = salemanID
        self.firstname = firstname
        self.lastname = lastname
        self.gender = gender
        self.photo = photo


    # getter method
    def get_salemanID(self):
        return self.salemanID

    # getter method
    def get_firstname(self):
        return self.firstname

    # getter method
    def get_lastname(self):
        return self.lastname

    # getter method
    def get_gender(self):
        return self.gender

    # getter method
    def get_photo(self):
        return self.photo

    # setter method
    def set_salemanID(self, salemanID):
        self.salemanID = salemanID

    # setter method
    def set_salemanID(self, salemanID):
        self.salemanID = salemanID

    # setter method
    def set_firstname(self, firstname):
        self.firstname = firstname

    # setter method
    def set_lastname(self, lastname):
        self.lastname = lastname

    # setter method
    def set_gender(self, gender):
        self.gender = gender

    # setter method
    def set_photo(self, photo):
        self.photo = photo

    def __str__(self):
        return self.salemanID + "," + self.firstname + "," + self.lastname + "," + self.gender + "," + self.photo + "."