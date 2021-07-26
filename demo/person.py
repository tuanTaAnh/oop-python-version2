
class Person:
    def __init__(self, Name, address, phone):
        self.Name = Name
        self.address = address
        self.address = address
        self.phone = phone

    # getter method
    def get_Name(self):
        return self.Name

    # getter method
    def get_address(self):
        return self.address

    # getter method
    def get_phone(self):
        return self.phone


    # setter method
    def set_Name(self, Name):
        self.Name = Name

    # setter method
    def set_address(self, address):
        self.address = address

    # setter method
    def set_phone(self, phone):
        self.phone = phone

    # def get_infor(self):
    #     return self.ID + "," + self.Name + "," + self.address + "," + self.phone + "."
    #
    # def get_infor_dist(self):
    #     return {
    #         "ID": self.ID,
    #         "Name": self.Name,
    #         "address": self.address,
    #         "phone": self.phone
    #     }