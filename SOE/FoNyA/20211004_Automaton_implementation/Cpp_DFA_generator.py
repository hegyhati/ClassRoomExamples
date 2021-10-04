import json

output = open("main.cpp","wt")
dfa = json.load(open("bab.json","rt"))

output.write(
"""
#include <iostream>
#include <string>
using namespace std;


int main() { 
"""    
)
output.write(f"    int state = {dfa['initial_state']};")
output.write(
"""
    string input;
    cin >> input;
    for (uint idx=0; idx<input.length(); idx++){
        switch(state){
"""
)
for state in dfa["states"]:
    output.write(f"            case {state}: switch (input[idx]) {{" + "\n")
    for symbol in dfa["alphabet"]:
        to=-1
        for transition in dfa["transitions"]:
            if transition["from"]==state and transition["with"]==symbol:
                to=transition["to"]
        output.write(f"                case '{symbol}': state = {to}; break;"+"\n")
    output.write("            } break;\n")
output.write(    
"""
        }
    }
    cout << ( (false """)
for accepting_state in dfa["accepting_states"]:
    output.write(f" || state=={accepting_state} ")

output.write(""")?"Accepted":"Not accepted") << endl;
}
"""
)

output.close()
