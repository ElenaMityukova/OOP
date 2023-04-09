class PhoneBook:
    def __init__(self):
        self.book = []

    def add_phone(self, phone):
        self.book.append(phone)

    def remove_phone(self, indx):
        self.book.pop(indx)

    def get_phone_list(self):
        return self.book


class PhoneNumber:
    def __init__(self, number, fio):
        self.number = number
        self.fio = fio
