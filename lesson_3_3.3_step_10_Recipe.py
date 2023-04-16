class Recipe:
    def __init__(self, *args):
        if len(args) == 0:
            self.cook = []
        else:
            self.cook = list(args)

    def add_ingredient(self, ing):
        self.cook.append(ing)

    def remove_ingredient(self, ing):
        if ing in self.cook:
            self.cook.remove(ing)

    def get_ingredients(self):
        return tuple(self.cook)

    def __len__(self):
        return len(self.cook)


class Ingredient:
    def __init__(self, name, volume, measure):
        self.name = name  # str
        self.volume = volume  # float
        self.measure = measure  # str

    def __str__(self):
        return f'{self.name}: {self.volume}, {self.measure}'


recipe = Recipe()
recipe.add_ingredient(Ingredient("Соль", 1, "столовая ложка"))
recipe.add_ingredient(Ingredient("Мука", 1, "кг"))
recipe.add_ingredient(Ingredient("Мясо баранины", 10, "кг"))
ings = recipe.get_ingredients()
print(*ings)
n = len(recipe)  # n = 3
print(n)
assert len(recipe) == 3