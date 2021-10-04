import json

class DFA:
    def __init__(self, filename:str) -> None:
        with open(filename) as file:
            self.data=json.load(file)
        self.__build_transition_cache()
        
    def __build_transition_cache(self) -> None:
        self.transitions = {}
        for transition in self.data["transitions"]:
            self.transitions[(transition["from"],transition["with"])]=transition["to"]
        print(self.transitions)

    def _delta(self, current_state:int, next_symbol:str) -> int:
        return self.transitions[(current_state,next_symbol)]

    def _delta_star(self,user_input:str) -> int:
        state = self.data["initial_state"]
        for symbol in user_input:
            state=self._delta(state, symbol)
        return state 
    
    def is_accepting_state(self, state:int):
        return state in self.data["accepting_states"]

    def is_accepted(self,user_input:str) -> bool:
        return self.is_accepting_state(self._delta_star(user_input))


if __name__ == "__main__":
    dfa = DFA("dfa_bab.json")
    while True:
        user_input = input("Please give me a word: ")
        if user_input=="": break
        print ( "Accepted." if dfa.is_accepted(user_input) else "Not accepted")



