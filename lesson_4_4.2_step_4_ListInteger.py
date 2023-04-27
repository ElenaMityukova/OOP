class ListInteger(list):
    def __init__(self, ints):
        for x in ints:
            self.__check_integer(x)
        super().__init__(ints)

    @staticmethod
    def __check_integer(value):
        if type(value) != int:
            raise TypeError('можно передавать только целочисленные значения')

    def __setitem__(self, key, value):
        self.__check_integer(value)
        super().__setitem__(key, value)

    def append(self, value):
        self.__check_integer(value)
        super().append(value)


s = ListInteger((1, 2, 3))
s[1] = 10
s.append(11)
print(s)
# s[0] = 10.5 # TypeError
