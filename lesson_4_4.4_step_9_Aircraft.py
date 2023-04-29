from typing import Union


class Aircraft:
    def __init__(self, model: str, mass: Union[int, float], speed: Union[int, float], top: Union[int, float]):
        self._check_model(model)
        self._check_plus_digits(mass)
        self._check_plus_digits(speed)
        self._check_plus_digits(top)

        self._model = model
        self._mass = mass
        self._speed = speed
        self._top = top

    def _check_model(self, value):
        if type(value) != str:
            raise TypeError('неверный тип аргумента')

    def _check_plus_digits(self, value):
        if value < 0:
            raise TypeError('неверный тип аргумента')

    def __setattr__(self, key, value):
        if key == "_model":
            self._check_model(value)
        if key in ("_mass", "_speed", "_top"):
            self._check_plus_digits(value)
        super().__setattr__(key, value)


class PassengerAircraft(Aircraft):
    def __init__(self, model, mass, speed, top, chairs):
        super().__init__(model, mass, speed, top)
        self._check_thing(chairs)
        self._chairs = chairs

    def _check_thing(self, value):
        if type(value) != int or value < 0:
            raise TypeError('неверный тип аргумента')


class WarPlane(Aircraft):
    def __init__(self, model, mass, speed, top, weapons):
        super().__init__(model, mass, speed, top)
        self._check_thing(weapons)
        self._weapons = weapons

    def _check_thing(self, value):
        if type(value) != dict:
            raise TypeError('неверный тип аргумента')


planes = [PassengerAircraft("МС-21", 1250, 8000, 12000.5, 140), \
          PassengerAircraft("SuperJet", 1145, 8640, 11034, 80), \
          WarPlane("Миг-35", 7034, 25000, 2000, {"ракета": 4, "бомба": 10}), \
          WarPlane("Су-35", 7034, 34000, 2400, {"ракета": 4, "бомба": 7})]

one = Aircraft("4", 1, 2, 3)
print(one.__dict__)
