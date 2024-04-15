lori = {
    "vertices" : ["Akos", "Adrian", "Attila", "Aron", "Dzseni"],
    "edges" : [
    #    Akos   Adrian Attila Aron   Dzseni
        [None,  True,  False, True,  False], # Akos
        [True,  None,  False, False, False], # Adrian
        [False, False, None,  True,  True ], # Attila
        [True,  False, True,  None,  True ], # Aron
        [False, False, True,  True,  None ]  # Dzseni
    ]
}

adrian = {
    "Akos" : ["Aron", "Adrian"],
    "Attila" : ["Aron", "Dzseni"],
    "Aron" : ["Attila", "Dzseni", "Akos"],
    "Adrian" : ["Akos"],
    "Dzseni" : ["Aron", "Attila"]
}



g = {
    "vertex_labels" : ["Akos", "Adrian", "Attila", "Aron", "Dzseni"],
    "graph": {
        0 : [3, 1],
        2 : [3, 4],
        3 : [2, 4, 0],
        1 : [0],
        4 : [3, 2]
    }
}

g2 = {
    "vertex_labels" : ["Akos", "Adrian", "Attila", "Aron", "Dzseni"],
    "graph": [
        [3, 1],
        [0],
        [3, 4],
        [2, 4, 0],
        [3, 2]
    ]
}

g2 = {
    "vertex_labels" : ["Akos", "Adrian", "Attila", "Aron", "Dzseni"],
    "graph": [
        {3, 1},
        {0},
        {3, 4},
        {2, 4, 0},
        {3, 2}
    ]
}

g3 = {
    "vertex_labels" : ["Akos", "Adrian", "Attila", "Aron", "Dzseni"],
    "edges": {
        (0,3), (0,1), (1,0), (2,3), (2,4), (3,2), (3,4), (3,0), (4,3), (4,2)
    }
}


g4 = {
    "vertex_labels" : ["Akos", "Adrian", "Attila", "Aron", "Dzseni"],
    "edges": {
        {0,3}, {0,1}, {2,3}, {2,4}, {3,4}
    }
}
