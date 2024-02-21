class PhoneNotFound(Exception):
    def __init__(self, message='Number not found'):
        self.message = message
        super().__init__(self.message)


class NameNotFound(Exception):
    def __init__(self, message='Name not found'):
        self.message = message
        super().__init__(self.message)


class BadBirthdayFormat(Exception):
    def __init__(self, message='Sorry, but birthday format is "DD.MM.YYYY"'):
        self.message = message
        super().__init__(self.message)


class BadEmailFormat(Exception):
    def __init__(self, message='Email format is incorrect, please try again'):
        self.message = message
        super().__init__(self.message)


class AddressIsExist(Exception):
    pass


class AddressIsNotExist(Exception):
    pass
