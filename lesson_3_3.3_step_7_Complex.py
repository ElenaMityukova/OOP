from math import sqrt

class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    @property
    def real(self):
        return self.__real

    @real.setter
    def real(self, value):
        if type(value) in (int, float):
            self.__real = value
        else:
            raise ValueError("Неверный тип данных.")

    @property
    def img(self):
        return self.__img

    @img.setter
    def img(self, value):
        if type(value) in (int, float):
            self.__img = value
        else:
            raise ValueError("Неверный тип данных.")

    def __abs__(self):
        return sqrt(self.__real * self.__real + self.__img * self.__img)


cmp = Complex(7, 8)
cmp.real = 3
cmp.img = 4
cmp_a = abs(cmp)
print(cmp_a)
