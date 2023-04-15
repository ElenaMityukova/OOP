class DigitRetrieve:
    def __init__(self):
        return

    def __call__(self, string, *args, **kwargs):
        digit = len(list(filter(lambda x: x.isdigit(), string)))
        digit1 = len(list(filter(lambda x: x.isdigit(), string[1:])))
        if digit == len(string) or digit1 == len(string[1:]) and string[0] == "-":
            return int(string)
        else:
            return None

dg = DigitRetrieve()
st = ["123", "abc", "-56.4", "0", "-5"]
digits = list(map(dg, st))  # [123, None, None, 0, -5]
print(*digits)