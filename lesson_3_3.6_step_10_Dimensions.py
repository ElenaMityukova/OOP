s_inp = "1 2 3; 4 5 6.78; 1 2 3; 1 1 2.5"


class Dimensions:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __setattr__(self, key, value):
        if value > 0:
            object.__setattr__(self, key, value)
        else:
            raise ValueError("габаритные размеры должны быть положительными числами")

    def __hash__(self):
        return hash((self.a, self.b, self.c))

    def __eq__(self, other):
        return hash(self) == hash(other)

lst_dims = []
s_inp = list(map(str.strip, s_inp.split(";")))

for line in s_inp:
    abc = []
    for num in line.split():
        if "." in num:
            abc.append(float(num))
        else:
            abc.append(int(num))
    a, b, c = abc
    print(abc)
    lst_dims.append(Dimensions(a, b, c))

for i in lst_dims:
    print(i.__dict__)

print(s_inp)
lst_dims = sorted(lst_dims, key=lambda x: hash(x))
for i in lst_dims:
    print(hash(i))

#for other results try these test data
#s_inp = "1 2 3; 4 5 6.78; 1 2 3; 0 1 2.5"
#s_inp = "1 2 3; 4 5 6.78; 1 2 3; -1 1 2.5"