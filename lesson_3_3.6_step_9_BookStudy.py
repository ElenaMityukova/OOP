class BookStudy:
    def __init__(self, name, author, year):
        self.name = name
        self.author = author
        self.year = year

    def __hash__(self):
        return hash((self.name.lower(), self.author.lower()))

    def __eq__(self, other):
        return hash(self) == hash(other)


lst_in = ["Python; Балакирев С.М.; 2020", "Python ООП; Балакирев С.М.; 2021", "Python ООП; Балакирев С.М.; 2022", "Python; Балакирев С.М.; 2021"]
lst_bs = []

for l in lst_in:
    args = list(map(str.strip, l.split(";")))
    args[-1] = int(args[-1])
    lst_bs.append(BookStudy(*args))

unique_books = 0
unique_lst = []
for book in lst_bs:
#    print(hash(book))
    if hash(book) not in unique_lst:
        unique_books += 1
        unique_lst.append(hash(book))

print(unique_books)
print([book.__dict__ for book in lst_bs])
