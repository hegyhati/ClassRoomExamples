from random import choice, uniform, choices

n = int(input("n= "))
m = int(input("m= "))

V = [f"v{i}" for i in range(n)]
E = {}
while len(E) != m:
    v1 = choice(V)
    v2 = choice(V)
    if v1 != v2:
        E[(v1,v2)] = uniform(1,100)

reach_test = choices(V,k=1000)
ditance_test = [(choice(V), choice(V)) for _ in range(1000)]

from weighted_digraph1 import Digraph as Digraph1
from weighted_digraph2 import Digraph as Digraph2
from weighted_digraph4 import Digraph as Digraph4
from datetime import datetime


digrpahs = [Digraph2(), Digraph4()]



for d in digrpahs:
    print(d)
    start = datetime.now()
    
    for v in V:
        d.add_vertex(v)
    for (f,t) in E:
        d.add_arc(f, t, E[(f,t)])
    
    mid = datetime.now()
    
    for v in reach_test:
        d.reachable_vertices(v)
    
    end = datetime.now()
    
    print("Grafepites: ", mid-start)
    print(f"{len(reach_test)} db melysegi bejaras:", end-mid)