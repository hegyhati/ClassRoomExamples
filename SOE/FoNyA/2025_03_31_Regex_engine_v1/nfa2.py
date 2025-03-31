# Sigma is lowercase ascii
# states are always 0, 1, 2, ...
# 0 is always the starint state


from string import ascii_lowercase

EMPTY = ""


class NFA:
    state_count : int
    transitions : set[tuple[int,str,int]]
    accepting_states : set[int]

    class AcceptedException(Exception):
        pass

    def __init__(self, acceptedstring:str):
        if acceptedstring == EMPTY:
            self.state_count = 1
            self.transitions = {}
            self.accepting_states = {0}
        else:
            self.state_count = 2
            self.transitions = {(0,acceptedstring,1)}
            self.accepting_states = {1}

    def __dfs_accept(self, state:int, remaining_input:str, last_state_since_empties: int):
        if  state in self.accepting_states and remaining_input == EMPTY: 
            raise NFA.AcceptedException()
        for (from_state, with_input, to_state) in self.transitions:
            if remaining_input.startswith(with_input) and from_state == state:
                if with_input != EMPTY:
                    self.__dfs_accept(to_state, remaining_input.removeprefix(with_input), to_state)
                elif to_state != last_state_since_empties:
                    self.__dfs_accept(to_state, remaining_input.removeprefix(with_input), last_state_since_empties)

    def accept(self, word:str) -> bool:
        for char in word:
            if char not in ascii_lowercase:
                raise ValueError("Only lowercase ascii letters accepted.")
        try:
            self.__dfs_accept(0, word, 0)
        except NFA.AcceptedException:
            return True
        return False
    
    def __str__(self):
         return f"""
                K = {{ {", ".join(str(q) for q in range(self.state_count))} }}
                d = {{ {", ".join(str(q) for q in self.transitions)} }}
                s = 0
                F = {{ {", ".join(str(q) for q in self.accepting_states)} }}
              """

    def __or__(self, other:"NFA"):
        shift_self = 1
        shift_other = 1 + self.state_count        
        union = NFA(EMPTY)
        union.state_count = 1+self.state_count+other.state_count
        union.accepting_states = {
            *{q + shift_self for q in self.accepting_states},
            *{q + shift_other for q in other.accepting_states}
        }
        union.transitions = { (0,EMPTY,shift_self),(0,EMPTY,shift_other),
            *{(p + shift_self, w, q + shift_self) for (p,w,q) in self.transitions},
            *{(p + shift_other, w, q + shift_other) for (p,w,q) in other.transitions}
        }
        return union

    def __add__(self, other:"NFA"):
        shift_other = self.state_count        
        concat = NFA(EMPTY)
        concat.state_count = self.state_count+other.state_count
        concat.accepting_states = {q + shift_other for q in other.accepting_states}
        concat.transitions = { 
            *self.transitions,
            *{(f,EMPTY,shift_other) for f in self.accepting_states},
            *{(p + shift_other, w, q + shift_other) for (p,w,q) in other.transitions}
        }
        return concat
    
    def kleene(self):
        starred = NFA(EMPTY)
        starred.state_count = self.state_count + 1
        starred.accepting_states = {0, *{ f + 1 for f in self.accepting_states}}
        starred.transitions = {
            (0,EMPTY,1), 
            *{(p+1,w,q+1) for (p,w,q) in self.transitions},
            *{(f+1,EMPTY, 1) for f in self.accepting_states}
        }
        return starred

                                                                            
                                                                            





