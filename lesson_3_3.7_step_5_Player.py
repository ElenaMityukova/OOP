import sys

lst_in = list(map(str.strip, sys.stdin.readlines()))
# ["Балакирев; 34; 2048", "Mediel; 27; 0", "Влад; 18; 9012", "Nina P; 33; 0"]

class Player:
    def __init__(self, name, old, score):
        self.name = name
        self.old = old
        self.score = score

    def __bool__(self):
        return int(self.score) > 0


players = []

for person in lst_in:
    name = person.split(";")[0]
    old = person.split(";")[1]
    score = person.split(";")[2]
    players.append(Player(name, old, score))

players_filtered = list(filter(lambda x: bool(x), players))