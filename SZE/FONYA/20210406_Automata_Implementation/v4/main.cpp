#include <iostream>
#include <string>
#include <set>
#include <map>
#include <vector>
using namespace std;

class DFA {
    public:
        using State=string;
        using Symbol=char;
        DFA(); // default bab DFA
        bool accept(const string& input) const;
    private:
        vector<State> K;
        map<State,int> KtoIdx;
        State s;
        set<State> F;
        vector< vector <int> > delta;
};

DFA::DFA() :
K({"semmi","van b", "van ba", "volt bab"}),
KtoIdx({{"semmi",0},{"van b",1},{"van ba",2},{"volt bab",3}}),
s("semmi"),
F({"volt bab"})
{
    vector<int> tmp;
    for (char c=0; c<127; ++c) tmp.push_back(0);
    delta.push_back(tmp);
    delta.push_back(tmp);
    delta.push_back(tmp);
    tmp.clear();
    for (char c=0; c<127; ++c) tmp.push_back(3);
    delta.push_back(tmp);
    delta[0]['b']=1;
    delta[1]['a']=2;
    delta[1]['b']=1;
    delta[2]['b']=3;
}


bool DFA::accept(const string& input) const {
    int current = KtoIdx.at(s);
    for(unsigned int i=0 ; i<input.length(); ++i)
        current = delta[current][input[i]];
    return F.find(K[current]) != F.end();
}



int main(){
    DFA has_bab;   
    string input;
    cin >> input; 
    cout << (has_bab.accept(input) ? "Elfogadva" : "Nem elfogadva") << endl;
}
