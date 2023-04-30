from typing import Any, Union


class Food:
    def __init__(self, name: str, weight: Union[int, float], calories: int):
        if type(name) == str:
            self._name = name
        if type(weight) in (int, float) and weight >= 0:
            self._weight = weight
        if type(calories) == int and calories >= 0:
            self._calories = calories


class BreadFood(Food):
    def __init__(self, name, weight, calories, white):
        super().__init__(name, weight, calories)
        if white in (True, False):
            self._white = white


class SoupFood(Food):
    def __init__(self, name, weight, calories, dietary):
        super().__init__(name, weight, calories)
        if dietary in (True, False):
            self._dietary = dietary


class FishFood(Food):
    def __init__(self, name, weight, calories, fish):
        super().__init__(name, weight, calories)
        if type(fish) == str:
            self._fish = fish
