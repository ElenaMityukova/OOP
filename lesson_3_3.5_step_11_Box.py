class Box:
    def __init__(self):
        self._in_box = []

    def add_thing(self, obj):
        self._in_box.append(obj)

    def get_things(self):
        return self._in_box

    def __eq__(self, other):
        if isinstance(other, Box):
            return all([True if x in other._in_box else False for x in self._in_box])


class Thing:
    def __init__(self, name, mass):
        self._name = name
        self._mass = mass

    def __eq__(self, other):
        return self._name.lower() == other._name.lower() and self._mass == other._mass


b1 = Box()
b2 = Box()

b1.add_thing(Thing('мел', 100))
b1.add_thing(Thing('тряпка', 200))
b1.add_thing(Thing('доска', 2000))

b2.add_thing(Thing('тряпка', 200))
b2.add_thing(Thing('мел', 100))
b2.add_thing(Thing('доска', 2000))

res = b1 == b2  # True

print(res)
