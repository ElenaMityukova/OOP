class Track:
    def __init__(self, start_x, start_y):
        self.start_x = start_x
        self.start_y = start_y
        self.tracks = []

    def add_point(self, x, y, speed):
        self.tracks.append([(x, y), speed])

    def check_it(self, indx):
        if not 0 <= indx < len(self.tracks):
            raise IndexError("некорректный индекс")

    def __getitem__(self, indx):
        self.check_it(indx)
        return self.tracks[indx]

    def __setitem__(self, indx, value):
        self.check_it(indx)
        self.tracks[indx][-1] = value


tr = Track(10, -5.4)
tr.add_point(20, 0, 100)  # первый линейный сегмент: indx = 0
tr.add_point(50, -20, 80)  # второй линейный сегмент: indx = 1
tr.add_point(63.45, 1.24, 60.34)  # третий линейный сегмент: indx = 2

tr[1] = 75
tr[2] = 60
c, s = tr[2]
print(c, s)

for item in tr.tracks:
    print(item)
