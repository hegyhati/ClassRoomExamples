#include <string>
#include <vector>
using namespace std;

struct Subject{
    string name;
    int limit;
};


Subject * parse() {
    Subject *s = new Subject();
    // do magic
    return s;
}

vector<vector<Subject*>> test(){
    Subject* s1 = parse();
    Subject* s2 = parse();

    vector<Subject*> gain;
    vector<Subject*> emo;

    gain.push_back(s1);  
    gain.push_back(s2); 
    s1->limit += 10; 
    emo.push_back(s1);

    return {gain, emo};
    // who cleans up and when?!

}

int main(){
    auto foo = test();
    return 0;
}