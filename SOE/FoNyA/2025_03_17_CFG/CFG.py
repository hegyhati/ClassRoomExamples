import json

class CFG:
    class Rule:
        def __init__(self, rulejson:list[str|list[str]]):
            if len(rulejson) != 2: raise ValueError
            self.LHS = rulejson[0]
            self.RHS = tuple(rulejson[1])
        def __str__(self):
            return self.LHS + " -> " + ("ϵ" if self.RHS == [] else " ".join(self.RHS))
        def __repr__(self):
            return str(self)
        def leftmost_apply_on(self, intermediate_word:list[str]):
            pos = intermediate_word.index(self.LHS)
            if pos == -1: return ValueError
            return intermediate_word[:pos] + list(self.RHS) + intermediate_word[pos+1:]

    def __check_consistency(self,data):
        if "terminals" not in data: raise ValueError
        if "non-terminals" not in data: raise ValueError
        if "rules" not in data: raise ValueError
        if "starting-non-terminal" not in data: raise ValueError
        if not isinstance(data["terminals"], list): raise ValueError
        # trallalalalla
        if set(data["terminals"]).intersection(data["non-terminals"]) != set(): raise ValueError("Non-terminals and terminals must be disjoint.")
        for rule in data["rules"]:
            if rule[0] not in data["non-terminals"]: raise ValueError("LHS of rule must be non-terminal")
            for symbol in rule[1]:
                if symbol not in data["non-terminals"] and symbol not in data["terminals"]: raise ValueError(f"Incorrect symbol {symbol} in rule {rule[0]} -> {' '.join(rule[1])}:")
        if data["starting-non-terminal"] not in data["non-terminals"]: raise ValueError("Incorrect starting symbol")


    def __init__(self, filename:str):
        with open(filename) as f:
            data = json.load(f)
        self.__check_consistency(data)
        self.terminals = set(data["terminals"])
        self.non_terminals = set(data["non-terminals"])
        self.rules = {
            non_terminal : {
                CFG.Rule(rule) 
                for rule in data["rules"] if rule[0] == non_terminal
            }
            for non_terminal in self.non_terminals
        }
        self.starting_non_terminal = data["starting-non-terminal"]

    
    
    def __recursive_search(self, intermediate_word: list[str], maxdepth:int, depth:int=0, debug:bool=False):
        if debug: print(" "*depth + " ".join(intermediate_word))
        if depth == maxdepth: return
        for symbol in intermediate_word:
            if symbol in self.non_terminals:
                for rule in self.rules[symbol]:
                    next_intermediate_word = rule.leftmost_apply_on(intermediate_word)
                    self.__recursive_search(next_intermediate_word, maxdepth, depth+1, debug)
                break
        else:
            print(f"New word found: {' '.join(intermediate_word)}")

    def demo_strings(self, depth:int):
        self.__recursive_search([self.starting_non_terminal], maxdepth=depth)

    def __input(self, word:str) -> list[str]:
        l = []
        word=word.strip()
        while word != "" :
            for terminal in sorted(self.terminals, key= lambda x: len(x), reverse=True):
                if word.startswith(terminal):
                    l.append(terminal)
                    word = word.removeprefix(terminal).strip()
                    break
            else: 
                raise ValueError("Incorrect input string")
        return l

    def __recursive_accept(self, remaining_input: list[str], stack: list[str]) -> bool:
        if set(stack).difference(remaining_input).difference(self.non_terminals) != set() : return False
        if len([s for s in stack if s in self.terminals]) > len(remaining_input): return False
        if stack == []: return remaining_input == []
        if stack[0] in self.terminals:
            if remaining_input == []: return False
            elif remaining_input[0] == stack[0]: return self.__recursive_accept(remaining_input[1:],stack[1:]) # Match, dynarray pop(0) nyeh...
            else: return False
        return any(self.__recursive_accept(remaining_input,rule.leftmost_apply_on(stack)) for rule in self.rules[stack[0]])

    def accept_DFS(self, word:str) -> bool:
        return self.__recursive_accept(self.__input(word),[self.starting_non_terminal])
    
    def accept_BFS(self, word:str) -> bool:
        word = self.__input(word)
        configurations = [(word,[self.starting_non_terminal])] # deque
        while configurations != []:
            (remaining_input, stack) = configurations.pop(0)
            if set(stack).difference(remaining_input).difference(self.non_terminals) != set() : continue 
            if len([s for s in stack if s in self.terminals]) > len(remaining_input): continue
            if stack == []: 
                if remaining_input == []: return True
                else: continue
            elif stack[0] in self.terminals:
                if remaining_input == []: continue
                elif remaining_input[0] == stack[0]: configurations.append((remaining_input[1:],stack[1:])) 
                else: continue
            else: # stack top is non-terminal
                for rule in self.rules[stack[0]]:
                    configurations.append((remaining_input,rule.leftmost_apply_on(stack)))
        return False

if __name__ == "__main__":
    g = CFG("numeric_expression_on_x.json")
    print(g.terminals, g.non_terminals, g.starting_non_terminal, g.rules)
    g.demo_strings(8)

    while True:
        s = input()
        print(g.accept_DFS(s))
        print(g.accept_BFS(s))




