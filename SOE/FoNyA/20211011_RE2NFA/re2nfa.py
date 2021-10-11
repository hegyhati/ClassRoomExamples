from nfa import NFA, dot_export


name_generator = None
def state_name() -> str:
    i = 0
    while True:
        yield "q"+str(i)
        i += 1


def symbol_2_nfa(symbol: str) -> NFA:
    start = next(name_generator)
    accept = next(name_generator)
    return NFA(
        states=[start, accept],
        transitions=[(start, symbol, accept)],
        starting_state=start,
        accepting_states=[accept],
    )

def star(nfa: NFA) -> NFA:
    starting = next(name_generator)
    return NFA(
        states=nfa.states + [starting],
        starting_state=starting,
        accepting_states=nfa.accepting_states + [starting],
        transitions=nfa.transitions + [
            (starting, "", nfa.starting_state)
        ] + [
            (accepting, "", nfa.starting_state) for accepting in nfa.accepting_states
        ]
    )

def union(nfa1: NFA, nfa2: NFA) -> NFA:
    starting = next(name_generator)
    return NFA(
        states=nfa1.states + nfa2.states + [starting],
        starting_state=starting,
        accepting_states=nfa1.accepting_states + nfa2.accepting_states,
        transitions=nfa1.transitions + nfa2.transitions + [
            (starting, "", nfa1.starting_state), (starting, "", nfa2.starting_state)
        ]
    )

def concat(nfa1: NFA, nfa2: NFA) -> NFA:
    return NFA(
        states=nfa1.states + nfa2.states,
        starting_state=nfa1.starting_state,
        accepting_states=nfa2.accepting_states,
        transitions=nfa1.transitions + nfa2.transitions + [
            (accepting, "", nfa2.starting_state) for accepting in nfa1.accepting_states
        ]
    )

def __re_2_nfa(re: list):
    
    if re[0] == ".":
        return concat(
            __re_2_nfa(re[1]),
            __re_2_nfa(re[2])
        )
    elif re[0] == "U":
        return union(
            __re_2_nfa(re[1]),
            __re_2_nfa(re[2])
        )
    elif re[0] == "*":
        return star(__re_2_nfa(re[1]))
    else:
        return symbol_2_nfa(re[0])

def re_2_nfa(re:list):
    global name_generator 
    name_generator = state_name()
    return __re_2_nfa(re)



if __name__ == "__main__":

    # (a U b)* a
    re = [".",
          ["*",
           ["U",
            "a",
            "b"]
           ],
          "a"
          ]

    nfa = re_2_nfa(re)

    print(nfa)

    dot_export(nfa, "(aUb)*a.dot")
