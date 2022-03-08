table  = [
    [None, 'a',  None, None, None ],
    [None, 'b',  None, None, None ],
    [None, None, 'w' , None, None ],
    [None, None, None, None, None ],
    [None, None, None, None, None ]
]
table[0][1] = 'x'

for sor in table:
    for mezo in sor:
        if mezo:
            print(mezo,end='')
        else:
            print('_', end='')
    print()