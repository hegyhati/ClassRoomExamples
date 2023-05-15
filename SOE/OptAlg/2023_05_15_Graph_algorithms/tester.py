from random import choice

n = int(input("n= "))
m = int(input("m= "))
# t = int(input("t= "))
testcount = 1000000

V = [f"v{i}" for i in range(n)]
E = []
while len(E) != m:
    v1 = choice(V)
    v2 = choice(V)
    if v1 != v2:
        E.append( (v1,v2) )

Test = [ (choice(V), choice(V)) for _ in range(testcount)]  

from digraph4 import Digraph
from datetime import datetime

d = Digraph()

start = datetime.now()

for v in V:
    d.add_vertex(v)
for (f,t) in E:
    d.add_arc(f, t)

mid = datetime.now()

for (f,t) in Test:
    d.has_arc(f,t)

end = datetime.now()

print("Grafepites: ", mid-start)
print(f"{testcount} db el lekerdezes:", end-mid)