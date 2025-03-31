from nfa2 import NFA

m = (NFA("a") | NFA("b")).kleene() + NFA("baba") + (NFA("a") | NFA("b")).kleene()

while True:
    print(m.accept(input()))


