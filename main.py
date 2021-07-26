from models.customer import Customer
from models.car import Car
from models.saleperson import SalePerson
from models.mechanic import Mechanic
from models.invoice import Invoice
from models.part import Part
from models.services import Service
from models.servicedetails import ServiceDetail
from models.serviceticket import ServiceTicket

def create_objects():
    # customerID, gender, age, address, city, postalcode, country, phone
    cus = Customer("123", "male", 18, "Duy Tan", "Ha Noi", "B123", "Viet Nam", "0326831080")
    print(cus)

    #serialnum, make, model, color, year, price
    car = Car("b1237", "camry", "toyata", "red", 2018, 10000)
    print(car)

    # salemanID, firstname, lastname, gender, photo
    saleper = SalePerson("234", "tuan", "ta anh", "male", "tuanta51.png")
    print(saleper)

    # mechanicID, lastname, firstname, birthdate
    mec = Mechanic("546", "A", "Nguyen Van", "20/11/2018")
    print(mec)

    #invoiceID, car, saleperson, customer, date
    inv = Invoice("981", car, saleper, cus, "11/1/2021")
    print(inv)

    # partID, name, description, price
    par = Part("x67", "banh xe", "banh vanh duc", 190)
    print(par)

    #serviceID, typ, price
    ser = Service("m89", "thay dau may xe", 20)
    print(ser)

    # serticID, car, customer, datein, dateout, status, totalcost
    serticket = ServiceTicket("123", car, cus, "12/2/2012", "2/2/2021", "hoan thien", 183)
    print(serticket)

    #serdetID, serviceticket, service, mechanic, part, quan_of_part, total_price
    serdetail = ServiceDetail("bx-678", serticket, ser, mec, par, 12, 120)





if __name__ == '__main__':
    create_objects()

