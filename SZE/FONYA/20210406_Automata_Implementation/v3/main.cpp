#include <iostream>
#include <string>
#include <set>
#include <map>
using namespace std;

class DFA {
    public:
        using State=int;
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
K({0,1,2,3}),
s(0),
F({3}),
delta({
   { {0,'b'} , 1 },
   { {1,'a'} , 2 },
   { {1,'b'} , 1 },
   { {2,'b'} , 3 }
})
{
    for(auto state: K) {
        for (char c=32; c<127; ++c) {
            if (delta.count({state,c})==0){
                delta[{state,c}]= state!=3 ? 0 : 3;
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
