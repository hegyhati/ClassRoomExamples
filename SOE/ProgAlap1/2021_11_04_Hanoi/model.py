def initial_state():
    return [[1, 2, 3], [], []]


def win(state):
    return len(state[0]) == 0 and len(state[2]) == 0

def good(state, move):
    from_column = state[move[0]]
    to_column = state[move[1]]
    if len(from_column) == 0:
        return False
    if len(to_column) == 0:
        return True
    return to_column[0] > from_column[0]


def apply(state, move):
    push(state[move[1]], pop(state[move[0]]))


def pop(column):
    top = column[0]
    del column[0]
    return top


def push(column, item):
    column.insert(0, item)

