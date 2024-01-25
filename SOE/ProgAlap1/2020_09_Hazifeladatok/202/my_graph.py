"""
Ez az osztaly egy graf tarolasara, piszkalasara lesz alkalmas.

Inicializlaskor megadhatunk egy kezdeti csucslistat. Ha ezt nem adjuk meg, akkor egy ures csucslistaval inicializal.

>>> g = Graph(['A','B','C'])

A `has_vertex` fuggveny visszaaadja, hogy egy csucs benne van-e a grafban, vagy sem:

>>> [g.has_vertex(x) for x in 'ABCDF']
[True, True, True, False, False]


Ujabb csucs adhato hozza az `add_vertex` fuggvennyel. Ha mar hozza volt adva, akkor nem tortenik semmi, es False-szal ter vissza, egyebkent True-val.

>>> g.add_vertex('A')
False
>>> g.add_vertex('D')
True

Az `add_edge` fuggvennyel (iranyitatlan) eleket adhatunk hozza. Ha az el mar letezik, akkor nem tortenik semmi, es ugyanugy True/False ertekkel ter vissza:


>>> g.add_edge('A','B')
True
>>> g.add_edge('B','C')
True
>>> g.add_edge('B','D')
True
>>> g.add_edge('D','C')
True
>>> g.add_edge('B','A')
False

Az `has_edge` fuggveny visszaaadja, hogy van-e el ket csucs kozott.

>>> g.has_edge('A','B')
True
>>> g.has_edge('B','A')
True
>>> for v1 in "ABCDE":
...     for v2 in "ABCDE":
...         if v1<v2 and g.has_edge(v1,v2):
...             print("{}-{}".format(v1,v2))
A-B
B-C
B-D
C-D

A `d` fuggveny visszaadja egy csucs szomszedinak a szamat. Ha a csucs nincs is a grafban, aadjon None-t vissza, ne 0-t.

>>> g.add_vertex('E')
True
>>> [g.d(v) for v in "ABCDEF"]
[1, 3, 2, 2, 0, None]

A `get_subgraph` visszaad egy reszgrafot, amiben csak a parameterben megadott csucsok, es az azokra illeszkedo elek vannak.

>>> g2=g.get_subgraph({'A','C','D'})
>>> for v1 in "ABCDE":
...     for v2 in "ABCDE":
...         if v1<v2 and g2.has_edge(v1,v2):
...             print("{}-{}".format(v1,v2))
C-D

>>> g3=g.get_subgraph({'B','C','A'})
>>> for v1 in "ABCDE":
...     for v2 in "ABCDE":
...         if v1<v2 and g3.has_edge(v1,v2):
...             print("{}-{}".format(v1,v2))
A-B
B-C

"""

class Graph:
    
    def __init__(self, vertices=[]):
        pass
    
    def has_vertex(self, vertex):
        pass
    
    def add_vertex(self, vertex):
        pass
    
    def add_edge(self,vertex1,vertex2):
        pass
    
    def has_edge(self,vertex1,vertex2):
        pass

    def d(self,vertex):
        pass
    
    def get_subgraph(self,vertices):
        pass
    