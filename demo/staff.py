from demo.person import Person

class Staff(Person):
    def __init__(self, staffID, Name, address, phone, salary):
        super().__init__(Name, address, phone)
        self.staffID = staffID
        self.salary = salary

    # getter method
    def get_staffID(self):
        return self.staffID

    # getter method
    def get_salary(self):
        return self.staffID

    # setter method
    def set_ID(self, staffID):
        self.staffID = staffID

    # setter method
    def set_salary(self, salary):
        self.salary = salary


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