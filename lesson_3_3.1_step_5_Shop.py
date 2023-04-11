class Shop:
    def __init__(self, name):
        self.name = name
        self.goods = []

    def add_product(self, product):
        self.goods.append(product)

    def remove_product(self, product):
        self.goods.remove(product)


class Product:
    uid = 1
    def __init__(self, name, weight, price):
        self.name = name
        self.weight = weight
        self.price = price
        self.id = Product.uid
        Product.uid += 1

    def __setattr__(self, key, value):
        if key == "id" and type(value) == int and value > 0 or key == "name" and type(value) == str or (key == "weight" or key == "price") and type(value) in (int, float) and value > 0:
            object.__setattr__(self, key, value)
        else:
            raise TypeError("Неверный тип присваиваемых данных.")

    def __delattr__(self, item):
        if item == "id":
            raise AttributeError("Атрибут id удалять запрещено.")
        object.__delattr__(self, item)


shop = Shop("Балакирев и К")
book = Product("Python ООП", 100, 1024)
shop.add_product(book)
shop.add_product(Product("Python", 150, 512))
for p in shop.goods:
    print(f"{p.id}. {p.name}, {p.weight}, {p.price}")
