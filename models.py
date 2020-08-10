import random
from random import randint


class BirthDate:
    def __init__(self):
        self.day = str(randint(1, 30))
        self.month = str(randint(1, 12))
        self.year = str(randint(1960, 2000))


class Account:
    def __init__(self, firstName, lastName, phoneNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.email = firstName + lastName + str(random.randint(100, 999999))
        self.password = "XY" + str(random.randint(1000, 99999)) + "YX"
        self.birthDate = BirthDate()
        self.phoneNumber = phoneNumber
