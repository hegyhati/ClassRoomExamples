#include <string>
#include <vector>
using namespace std;

struct Subject{
    string name;
    int limit;
};



int main(){
    Subject s1;
    Subject s2;

    vector<Subject> gain;
    vector<Subject> emo;

    gain.push_back(s1); //  COPY
    s1.limit += 10; // gain-t nem erinti

}