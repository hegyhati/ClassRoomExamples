#include <iostream>
#include <string>
#include <set>
#include <map>
using namespace std;

class DFA {
    public:
        using State=string;
        using Symbol=char;
        DFA(); // default bab DFA
        bool accept(const string& input) const;
    private:
        set<State> K;
        State s;
        set<State> F;
        map< pair<State,Symbol>, State> delta;
};

DFA::DFA() :
K({"semmi","van b", "van ba", "volt bab"}),
s("semmi"),
F({"volt bab"}),
delta({
   { {"semmi",'b'} , "van b" },
   { {"van b",'a'} , "van ba" },
   { {"van b",'b'} , "van b" },
   { {"van ba",'b'} , "volt bab" }
})
{
    for(auto state: K) {
        for (char c=32; c<127; ++c) {
            if (delta.count({state,c})==0){
                delta[{state,c}]= state!="volt bab" ? "semmi" : "volt bab";
            }
        }
    }
}


bool DFA::accept(const string& input) const {
    State current = s;
    for(unsigned int i=0 ; i<input.length(); ++i)
        current = delta.at({current,input[i]});
    return F.find(current) != F.end();
}



int main(){
    DFA has_bab;   
    string input;
    cin >> input; 
    cout << (has_bab.accept(input) ? "Elfogadva" : "Nem elfogadva") << endl;
}
