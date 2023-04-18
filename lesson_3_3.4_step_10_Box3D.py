class Box3D:
    def __init__(self, width, height, depth):
        self.width = width
        self.height = height
        self.depth = depth

    def __add__(self, other):
        return Box3D(self.width + other.width, self.height + other.height, self.depth + other.depth)

    def __radd__(self, other):
        return Box3D(other.width + self.width, other.height + self.height, other.depth + self.depth)

    def __sub__(self, other):
        return Box3D(self.width - other.width, self.height - other.height, self.depth - other.depth)

    def __rsub__(self, other):
        return Box3D(other.width - self.width, other.height - self.height, other.depth - self.depth)

    def __mul__(self, other):
        if type(other) in (int, float):
            return Box3D(self.width * other, self.height * other, self.depth * other)
        else:
            return Box3D(self.width * other.width, self.height * other.height, self.depth * other.depth)

    def __rmul__(self, other):
        if type(other) in (int, float):
            return Box3D(other * self.width, other * self.height, other * self.depth)
        else:
            return Box3D(self.width * other.width, self.height * other.height, self.depth * other.depth)

    def __floordiv__(self, other):
        if type(other) in (int, float):
            return Box3D(self.width // other, self.height // other, self.depth // other)
        else:
            return Box3D(self.width // other.width, self.height // other.height, self.depth // other.depth)

    def __rfloordiv__(self, other):
        if type(other) in (int, float):
            return Box3D(other // self.width, other // self.height, other // self.depth)
        else:
            return Box3D(self.other // self.width, self.other // self.height, self.other // self.depth)

    def __mod__(self, other):
        if type(other) in (int, float):
            return Box3D(self.width % other, self.height % other, self.depth % other)
        else:
            return Box3D(self.width % other.width, self.height % other.height, self.depth % other.depth)

    def __rmod__(self, other):
        if type(other) in (int, float):
            return Box3D(other % self.width, other % self.height, other % self.depth)
        else:
            return Box3D(self.other % self.width, self.other % self.height, self.other % self.depth)


box1 = Box3D(1, 2, 3)
box2 = Box3D(2, 4, 6)

box = box1 + box2  # Box3D: width=3, height=6, depth=9 (соответствующие размерности складываются)
print(box.__dict__)
box = box1 * 2  # Box3D: width=2, height=4, depth=6 (каждая размерность умножается на 2)
print(box.__dict__)
box = 3 * box2  # Box3D: width=6, height=12, depth=18
print(box.__dict__)
box = box2 - box1  # Box3D: width=1, height=2, depth=3 (соответствующие размерности вычитаются)
print(box.__dict__)
box = box2 % 3  # Box3D: width=2, height=1, depth= При каждой арифметической операции следует создавать новый объект класса Box3D с соответствующими значениями локальных атрибутов.
print(box.__dict__)