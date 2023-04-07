class RadiusVector2D:
    def __init__(self, x=0, y=0):
        self.__x = self.__y = 0
        self.x = x
        self.y = y

    MIN_COORD = -100
    MAX_COORD = 1024

    @classmethod
    def __is_ok(cls, x):
        return type(x) in (int, float) and cls.MIN_COORD <= x <= cls.MAX_COORD

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if self.__is_ok(value):
            self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if self.__is_ok(value):
            self.__y = value

    @staticmethod
    def norm2(vector):
        return vector.x * vector.x + vector.y * vector.y


# try this example
first_vector = RadiusVector2D(5, 10)
print(first_vector.__dict__)
print(RadiusVector2D.norm2(first_vector))

second_vector = RadiusVector2D(2)
print(second_vector.__dict__)
print(RadiusVector2D.norm2(second_vector))

third_vector = RadiusVector2D()
print(third_vector.__dict__)
print(RadiusVector2D.norm2(third_vector))

false_vector = RadiusVector2D(-105, 1900)
print(false_vector.__dict__)
print(RadiusVector2D.norm2(false_vector))
