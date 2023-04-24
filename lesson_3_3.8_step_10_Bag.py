class Bag:
    def __init__(self, max_weight):
        self.max_weight = max_weight
        self.weight = 0
        self.bag = []

    def check_weight(self, new_thing, old_thing=None):
        w = new_thing.weight + self.weight if old_thing is None else new_thing.weight + self.weight - old_thing.weight
        if w > self.max_weight:
            raise ValueError('превышен суммарный вес предметов')

    def check_index(self, index):
        if not (0 <= index < len(self.bag)):
            raise IndexError('неверный индекс')

    def add_thing(self, thing):
        self.check_weight(thing)
        self.bag.append(thing)
        self.weight += thing.weight

    def __getitem__(self, indx):
        self.check_index(indx)
        return self.bag[indx]

    def __setitem__(self, key, value):
        self.check_index(key)
        changing_th = self.bag[key]
        self.check_weight(value, changing_th)
        self.bag[key] = value
        self.weight += (value.weight - changing_th.weight)

    def __delitem__(self, key):
        if not isinstance(key, int):
            raise TypeError('должно быть указано число')
        self.check_index(key)
        thing_tb_del = self.bag.pop(key)
        self.weight -= thing_tb_del.weight


class Thing:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight


bag = Bag(1000)
bag.add_thing(Thing('книга', 100))
bag.add_thing(Thing('носки', 200))
bag.add_thing(Thing('рубашка', 500))
bag.add_thing(Thing('ножницы', 300)) # генерируется исключение ValueError
print(bag[2].name) # рубашка
bag[1] = Thing('платок', 100)
print(bag[1].name) # платок
del bag[0]
print(bag[0].name) # платок


