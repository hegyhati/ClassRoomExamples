class LLItem:
    value: int
    next: "LLItem"



# Felepul a h1, h2 lista
h1 = ...
h2 = ...

merged = None
last = None

while h1 is not None and h2 is not None:
    if h1.value < h2.value:
        if merged is None:
            merged = h1
            last = h1
        else:
            last.next = h1
            last = last.next
        h1 = h1.next
    else:
        if merged is None:
            merged = h2
            last = h2
        else:
            last.next = h2
            last = last.next
        h2 = h2.next
if h1 is None:
    last.next = h2
    h2 = None
else:
    last.next = h1
    h1 = None