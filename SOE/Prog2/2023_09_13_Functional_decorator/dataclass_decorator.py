from dataclasses import dataclass, field

@dataclass(frozen=True)
class Book:
    author : str
    title : str
    publish_year : int
    publisher : str
    pages : int
    ISBN : str = field(compare=False, default="Not defined")

hp1 = Book("J.K. Rowling", "Harry Potter and the Philosphers stone", 1998, "whoknows", 654, "???")
print(hp1)

hp2 = Book("J.K. Rowling", "Harry Potter and the Philosphers stone", 1998, "whoknows", 654)
# hp2.title = "Harry Potter and the Sorcerers stone"
# ha frozen, akkor nem megy

read_count = {hp1: 3, hp2: 1}
# csak akkor, ha frozen

if (hp1 == hp2):
    print("Ugyanaz")