class ShopItem:
    def __init__(self, name, weight, price):
        self.name = name
        self.weight = weight
        self.price = price

    def __hash__(self):
        return hash((self.name, self.weight, self.price))

    def __eq__(self, other):
        return hash(self) == hash(other)


lst_in = ["Системный блок: 1500 75890.56", "Монитор Samsung: 2000 34000", "Клавиатура: 200.44 545", "Монитор Samsung: 2000 34000"]

shop_items = {}

for i in lst_in:
    name = i.split(":")[0]
    weight = i.split(":")[1].split()[0]
    price = i.split(":")[1].split()[1]
    item = ShopItem(name, weight, price)
    total = 1
    if type(item) == ShopItem and hash(item) in shop_items:
        shop_items[hash(item)] = [item, total + 1]
    else:
        shop_items[hash(item)] = [item, total]

it1 = ShopItem('name', 10, 11)
it2 = ShopItem('NAME', 10, 11)

name = lst_in[0].split(':')
for sp in shop_items.values():
    print(type(sp[0]), sp[1])

v = list(shop_items.values())
if v[0][0].name.strip() == "Системный блок":
    print(v[0][1], v[1][1], v[2][1], len(v))
