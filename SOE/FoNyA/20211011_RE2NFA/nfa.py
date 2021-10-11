from typing import Counter


class NFA:
    counter = 1

    def __init__(self, states, transitions, starting_state, accepting_states) -> None:
        self.states = states
        self.transitions = transitions
        self.starting_state = starting_state
        self.accepting_states = accepting_states
    
    def __str__(self) -> str:
        return " states: " + str(self.states) \
        + "\n starting: " + self.starting_state \
        + "\n transitions: " + str(self.transitions) \
        + "\n accepting: " + str(self.accepting_states) 





def dot_export(nfa: NFA, filename: str):
    with open(filename,"wt") as f:
        f.write('digraph{\n')
        f.write(' rankdir="LR"\n')
        f.write(' node [shape = circle]\n')
        f.write(' start  [label = "", shape=none, width=0]\n')
        for state in nfa.accepting_states:
            f.write(f" {state} [ shape=doublecircle ] \n")
        f.write(f" start -> {nfa.starting_state}\n")
        for (s,w,t) in nfa.transitions:
            f.write(f" {s} -> {t} [label=\"{'ϵ' if w == '' else w}\"]\n")
        f.write('}\n')



