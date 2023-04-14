class Dimensions:
    MIN_DIMENSION = 10
    MAX_DIMENSION = 1000

    def __init__(self, a, b, c):
        self.__a = self.__b = self.__c = None
        self.a = a
        self.b = b
        self.c = c

    @classmethod
    def size(cls, value):
        return type(value) in (int, float) and cls.MIN_DIMENSION <= value <= cls.MAX_DIMENSION

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, value):
        self.__a = value

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, value):
        self.__b = value

    @property
    def c(self):
        return self.__c

    @c.setter
    def c(self, value):
        self.__c = value

    def __setattr__(self, key, value):
        if key == "MIN_DIMENSION" or key == "MAX_DIMENSION":
            raise AttributeError("Менять атрибуты MIN_DIMENSION и MAX_DIMENSION запрещено.")
        if self.size(value):
            super().__setattr__(key, value)
