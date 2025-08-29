circle = '◖◗'
black = f'\033[0;30;47m{circle}\033[0;32;42m'
white = f'\033[0;37;40m{circle}\033[0;32;42m'
nothing = f'\033[0;32;42m{circle}\033[0;32;42m'

def kirajzol(tabla):
    print('     ', end='')
    for oszlop in range(len(tabla[0])):
        print(f'{oszlop+1:2}', end='')
    print()
    for idx, sor in enumerate(tabla):
        print(f"{idx+1:4} ", end='')
        for mezo in sor:
            if mezo:
                print(mezo, end='')
            else:
                print(nothing, end='')
        print('\033[1;37;40m')

tabla = [
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, black, white, None, None, None],
    [None, None, None, white, black, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None]
]

kirajzol(tabla)

sor = int(input('Sor: '))
oszlop = int(input('Oszlop: '))
tabla[sor-1][oszlop-1] = black

kirajzol(tabla)