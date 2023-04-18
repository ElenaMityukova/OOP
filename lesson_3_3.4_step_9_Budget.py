class Budget:
    def __init__(self):
        self.budget = []

    def add_item(self, it):
        self.budget.append(it)

    def remove_item(self, indx):
        self.budget.pop(indx)

    def get_items(self):
        return self.budget


class Item:
    def __init__(self, name, money):
        self.name = name
        self.money = money

    def __add__(self, other):
        if type(other) in (int, float):
            return self.money + other
        elif type(other) == Item:
            return self.money + other.money

    def __radd__(self, other):
        if type(other) in (int, float):
            return other + self.money


my_budget = Budget()
my_budget.add_item(Item("Курс по Python ООП", 2000))
my_budget.add_item(Item("Курс по Django", 5000.01))
my_budget.add_item(Item("Курс по NumPy", 0))
my_budget.add_item(Item("Курс по C++", 1500.10))

# вычисление общих расходов
s = 0
for x in my_budget.get_items():
    s = s + x
    print(s)