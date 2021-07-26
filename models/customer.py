
class Customer:
    def __init__(self, customerID, gender, age, address, city, postalcode, country, phone):
        self.customerID = customerID
        self.gender = gender
        self.age = age
        self.address = address
        self.city = city
        self.postalcode = postalcode
        self.country = country
        self.phone = phone


    # getter method
    def get_customerID(self):
        return self.customerID

    # getter method
    def get_gender(self):
        return self.gender

    # getter method
    def get_age(self):
        return self.age

    # getter method
    def get_address(self):
        return self.address

    # getter method
    def get_city(self):
        return self.city

    # getter method
    def get_postalcode(self):
        return self.postalcode

    # getter method
    def get_address(self):
        return self.address

    # getter method
    def get_phone(self):
        return self.phone

    # setter method
    def set_customerID(self, customerID):
        self.customerID = customerID

    # setter method
    def set_gender(self, gender):
        self.gender = gender

    # setter method
    def set_age(self, age):
        self.age = age

    # setter method
    def set_address(self, address):
        self.address = address

    # setter method
    def set_city(self, city):
        self.city = city

    # setter method
    def set_postalcode(self, postalcode):
        self.postalcode = postalcode

    # setter method
    def set_country(self, country):
        self.country = country

    # setter method
    def set_phone(self, phone):
        self.phone = phone

    def __str__(self):
        return self.customerID + "," + self.gender + "," + str(self.age) + "," + self.address + "," + self.city +  "," + self.postalcode +  "," + self.country +  "," + self.phone +  "."