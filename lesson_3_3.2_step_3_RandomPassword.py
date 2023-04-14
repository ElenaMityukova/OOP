from random import randint, sample

class RandomPassword:
    def __init__(self, psw_chars, min_length, max_length):
        self.psw_chars = psw_chars
        self.min_length = min_length
        self.max_length = max_length

    def __call__(self, *args, **kwargs):
        length = randint(self.min_length, self.max_length)
        return "".join(sample(self.psw_chars, length))

rnd = RandomPassword("qwertyuiopasdfghjklzxcvbnm0123456789!@#$%&*", 5, 20)
lst_rnd = [rnd() for _ in range(3)]

print(*lst_rnd)