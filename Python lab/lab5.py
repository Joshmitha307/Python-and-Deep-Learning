
#Person class is the base class for other classes
class Person():  #Person class

    # initalising the __init__ constructor
    def __init__(self,name,age,phone_number):
        self.name = name
        self.age = age
        self.phone_number = phone_number
        #semi private variable or protected
        self._gender = "not_metioned"
        print("Person instance is created")

    #Printing the person details
    def get_details(self):
        print("Name - {self.name}\nAge - {self.age}\nPhone Number - {self.phone_number}")

    #creating a method for initialising semi private data member
    def set_person_gender(self, gender):
            self._gender = gender

    #creating a method for initialising semi private data member
    def get_person_gender(self):
        return self._gender

#flight class
class Flight():

    # initalising the __init__ constructor
    def __init__(self, flight_name,flight_number):
        self.flight_name = flight_name
        self.flight_number = flight_number
        print("Flight instance created")

#implementing inheritance
class Employee(Person):

    # initalising the __init__ constructor
    def __init__(self,name,age,phone_number,employeeID):
        Person.__init__(self,name,age,phone_number)
        self.employeeID = employeeID
        print("Employee instance created")
        #super.__init__(name,age,phone_number)

    # using a super() keyword to call method in parent class
    def print_passenger_details(self):
        super.details()

#Implemented multiple Inhertence
class Ticket(Flight,Person):

    # initalising the __init__ constructor
    def __init__(self,ticket_number,departure_date):
        self.ticket_number = ticket_number
        self.departure_date = departure_date



#Implemented multiple Inhertence
class Passenger(Person,Flight):

    # initalising the __init__ constructor
    def __init__(self,name,age,phone_number,luggage_weight):
        Person.__init__(self, name, age, phone_number)
        self.luggage_weight = luggage_weight

        #creating private variable
        self.__passenger_passport_number = "not updated"

    #creating a method for initialising private data member
    def set_passport_number(self,passport_number):
        self.__passenger_passport_number = passport_number

    #creating a method for retrieving private data member
    def get_passport_number(self):
        return self.__passenger_passport_number

#creating the instance of Person class
person1 = Person('ram',55,1234567890)

#initialising the semi private variable or protected
person1.set_person_gender('male')

#printing the semi  private variable
print(person1.get_person_gender())

#other way to print semi private variable(not recommended)
print(person1._gender)

#creating the instance of Employee class
employee1 = Employee("Vineeth",22,1234567890,'14b81a12b6')
employee2 = Employee("Raghu",33,1234567890,'14b81a12c0')

#super call
employee1.get_details()


#creating the instance of Passenger class
passenger1 = Passenger("Ratan",33,1234567890,67)

#initialising the semi private variable or protected
passenger1.set_passport_number('AA123456')

#printing the private variable
print(passenger1.get_passport_number())

#other way to print private variable(not recommended
#print(passenger1._Passenger__passport_number)   #not working