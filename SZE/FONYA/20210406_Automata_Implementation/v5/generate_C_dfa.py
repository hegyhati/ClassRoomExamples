import json

f = open("bab.json","rt")
dfa = json.load(f)

out = open("bab.c","wt")

out.write("int accept(char* input) {\n")
out.write("    int state;\n")
out.write("    for (state={}; *input != '\\0'; ++input){{\n".format(dfa["K"].index(dfa["s"])))
out.write("        switch(state){\n")
for state in dfa["K"]:
    out.write("            case {}: switch(*input) {{\n".format(dfa["K"].index(state)))
    for symbol,targetstate in dfa["delta"][state].items():
        if symbol != "_":
            out.write("                    case '{}' : state={}; break;\n".format(symbol,dfa["K"].index(targetstate)))
    out.write("                    default: state={};\n".format(dfa["K"].index(dfa["delta"][state]["_"])))
    out.write("                }; break;\n")
out.write("        }\n")
out.write("    }\n")
out.write("    return 0")
for accepting in dfa["F"]:
    out.write(" || state=={}".format(dfa["K"].index(accepting)))
out.write(";\n")
out.write("}\n")
