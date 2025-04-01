#include <string>
#include <vector>
using namespace std;

struct Subject{
    string name;
    int limit;
};

struct SubjectWrapper{
    int* reference_count;
    Subject* pointer;

    SubjectWrapper() {
        reference_count =  new int;
        *reference_count = 1;
        pointer = new Subject();
    } 
    SubjectWrapper(const SubjectWrapper& other) {
        reference_count = other.reference_count;
        pointer = other.pointer;
        (*reference_count)++;
    }
    // assignment operator =
    ~SubjectWrapper(){
        (*reference_count) --;
        if (*reference_count == 0) {
            delete reference_count;
            delete pointer;
        }
    } 

    Subject& operator*(void) {
        return *pointer;
    }
};


SubjectWrapper parse() {
    SubjectWrapper s = SubjectWrapper();
    // do magic
    return s;
}

vector<vector<SubjectWrapper>> test(){
    SubjectWrapper s1 = parse();
    SubjectWrapper s2 = parse();

    vector<SubjectWrapper> gain;
    vector<SubjectWrapper> emo;

    gain.push_back(s1); 
    gain.push_back(s2); 
    (*s1).limit += 10; 
    emo.push_back(s1);

    return {gain, emo};
}


int main(){
    auto foo = test();
    return 0;
}