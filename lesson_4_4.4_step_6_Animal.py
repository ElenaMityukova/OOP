class AnimalDescriptor:

    def __set_name__(self, owner, name):
        self.name = f'_{owner.__name__}__{name}'

    def __get__(self, instance, owner=None):
        return property() if instance is None else getattr(instance, self.name)

    def __set__(self, instance, value):
        setattr(instance, self.name, value)


class Animal:
    name = AnimalDescriptor()
    kind = AnimalDescriptor()
    old = AnimalDescriptor()

    def __init__(self, name, kind, old):
        self.__name, self.__kind, self.__old = name, kind, old

animals = [Animal("Васька", "дворовый кот", 5), Animal("Рекс", "немецкая овчарка", 8), Animal("Кеша", "попугай", 3)]
