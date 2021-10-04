def delta(current_state, next_symbol):
    for transition in dfa["transitions"]:
        if transition["from"]==current_state and transition["with"]==next_symbol:
            return transition["to"]
    raise ValueError(f"Invalid symbol: {next_symbol}.")


import json

user_input = input("Please give me a word: ")

dfa = json.load(open("dfa_bab.json","rt"))

state = dfa["initial_state"]
for symbol in user_input:
    state=delta(state, symbol)
print ( "Accepted." if state in dfa["accepting_states"] else "Not accepted")


