class Bag:
    def __init__(self, max_weight):
        self.max_weight = max_weight
        self.__things = []

    @property
    def things(self):
        return self.__things

    def add_thing(self, thing):
        total = self.get_total_weight()
        if total + thing.weight <= self.max_weight:
            self.__things.append(thing)

    def remove_thing(self, indx):
        self.__things.pop(indx)

    def get_total_weight(self):
        return sum(i.weight for i in self.__things)


class Thing:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
