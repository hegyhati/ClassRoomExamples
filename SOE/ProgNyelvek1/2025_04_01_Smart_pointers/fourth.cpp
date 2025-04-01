#include <string>
#include <vector>
#include <memory>
using namespace std;

struct Subject{
    string name;
    int limit;
};


std::shared_ptr<Subject> parse() {
    std::shared_ptr<Subject> s = std::make_shared<Subject>();
    // do magic
    return s;
}

vector<vector<shared_ptr<Subject>>> test(){
    std::shared_ptr<Subject> s1 = parse();
    std::shared_ptr<Subject> s2 = parse();

    vector<std::shared_ptr<Subject>> gain;
    vector<std::shared_ptr<Subject>> emo;

    gain.push_back(s1); //  
    gain.push_back(s2); //  
    (*s1).limit += 10; //
    emo.push_back(s1);

    return {emo, gain};
}

int main() {
    auto ize = test();
    return 0;
}