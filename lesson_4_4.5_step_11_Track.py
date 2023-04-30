class Track:
    def __init__(self, *args):
        if isinstance(args[0], PointTrack):
            self.__points = list(args)
        else:
            if len(args) == 2:
                x, y = args
                self.__points = [PointTrack(x, y)]

    @property
    def points(self):
        return tuple(self.__points)

    @points.setter
    def points(self, value):
        self.points = value

    def add_back(self, pt):
        self.__points.append(pt)

    def add_front(self, pt):
        self.__points.insert(0, pt)

    def pop_back(self):
        self.__points.pop()

    def pop_front(self):
        self.__points.pop(0)


class PointTrack(Track):
    def __init__(self, x, y):
        self.check_it(x)
        self.check_it(y)
        self._x = x
        self._y = y

    def check_it(self, value):
        if type(value) not in (int, float):
            raise TypeError('координаты должны быть числами')

    def __str__(self):
        return f"PointTrack: {self._x}, {self._y}"


tr = Track(PointTrack(0, 0), PointTrack(1.2, -0.5), PointTrack(2.4, -1.5))
tr.add_back(PointTrack(1.4, 0))
tr.pop_front()
for pt in tr.points:
    print(pt)
