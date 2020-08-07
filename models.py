from random import randint


class BirthDate:
    def __init__(self):
        self.day = str(randint(1, 30))
        self.month = str(randint(1, 12))
        self.year = str(randint(1960, 2000))


class Account:
    def __init__(self, firstName, lastName, email, password, birthDate):
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.password = password
        self.birthDate = birthDate
