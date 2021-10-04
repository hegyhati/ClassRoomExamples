import json

class NFA:

    class AcceptedException(Exception):
        pass

    def __init__(self, filename:str, verbose=False) -> None:
        self.verbose=verbose
        with open(filename) as file:
            self.data=json.load(file)

    def __traverse(self,user_input:str) -> None:
        self.__visited_configurations = set()
        self.__recursive_traverse(self.data["initial_state"],user_input)
    
    def __recursive_traverse(self,current_state,remaining_input:str, depth=0):
        visited = (current_state,remaining_input) in self.__visited_configurations
        if self.verbose:
            print(" "*depth + f"({current_state},'{remaining_input}')" + (" ~~ already examined" if visited else ""))
        if visited: return
        self.__visited_configurations.add((current_state,remaining_input))
        if self.is_accepting_state(current_state) and remaining_input=="":
            raise NFA.AcceptedException
        for transition in self.data["transitions"]:
            if current_state == transition["from"] and remaining_input.startswith(transition["with"]):
                self.__recursive_traverse(transition["to"],remaining_input[len(transition["with"]):],depth+1)
    
    def is_accepting_state(self, state):
        return state in self.data["accepting_states"]

    def is_accepted(self,user_input:str) -> bool:
        try:
            self.__traverse(user_input)
        except NFA.AcceptedException:
            return True
        return False

if __name__ == "__main__":
    nfa = NFA("nfa_example.json", verbose=True)
    while True:
        user_input = input("Please give me a word: ")
        if user_input=="": break
        print ( "Accepted." if nfa.is_accepted(user_input) else "Not accepted")



