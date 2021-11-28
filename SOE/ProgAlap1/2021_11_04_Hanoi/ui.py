def display(state):
    for column in state:
        fancy_display(column)

def fancy_display(column):
    print()
    if len(column) == 0:
        print("━\n")
        return
    n = column[-1]
    for r in range(2*n-1):
        for c in range(2*len(column)):
            if c%2 == 0:
                print("━" if r == n-1  else " ", end="")
            else:
                disk = column[-1-c//2]
                print("█" if - disk < r - (n-1) < disk else " ", end="")
        print()
    print()


def get_move():
    return (int(input("Honnan? ")), int(input("Hova? ")))
