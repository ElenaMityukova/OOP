class Lib:
    def __init__(self):
        self.book_list = []

    def get_list(self):
        return self.book_list

    def __add__(self, other):
        self.book_list = self.book_list + [other]
        return self

    def __radd__(self, other):
        self.book_list = [other] + self.book_list
        return self

    def __sub__(self, other):
        if type(other) == Book:
            self.book_list.remove(other)
            return self

        elif type(other) == int:
            self.book_list.pop(other)
            return self

    def __len__(self):
        return len(self.book_list)


class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

lib = Lib()

lib = lib + Book("Философия", "Аристотель", 1990)
lib += Book("Простой Python", "Билл Любанович", 2020)
lib += Book("Тестирование Дот Ком", "Роман Савин", 2008)
print(len(lib))
for b in lib.get_list():
    print(b.__dict__)