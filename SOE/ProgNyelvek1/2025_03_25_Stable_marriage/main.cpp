#include <fstream>
#include <string>
#include <iostream>
#include <map>
#include <vector>

using std::cerr;

struct problem {
    std::map<std::string,std::vector<std::string>> girls;
    std::map<std::string,std::vector<std::string>> boys;
};


problem load_input(std::string filename) {
    std::fstream f(filename);
    problem p;

    std::string token;
    f >> token;
    while(true) {
        f >> token;
        if (token == "BOYS:") break;
        auto& girl = p.girls[token] = std::vector<std::string>();
        while (true) {
            f >> token;
            if (token == "END") break;
            girl.push_back(token);
        } 
    }
    while(true) {
        f >> token;
        if (token == "END") break;
        auto& boy = p.boys[token] = std::vector<std::string>();
        while (true) {
            f >> token;
            if (token == "END") break;
            boy.push_back(token);
        } 
    }
    return p;
}

void test_print(const problem& p){
    cerr << "Girls: \n";
    for ( const auto& [girl, boys]: p.girls ){
        cerr << girl << " : ";
        for (const auto& boy: boys)
            cerr << boy << " -> ";
        cerr << "\n";
    }   
    cerr << "Boys: \n";
    for ( const auto& [boy, girls]: p.boys ){
        cerr << boy << " : ";
        for (const auto& girl: girls)
            cerr << girl << " -> ";
        cerr << "\n";
    }   
}


int main() {
    auto test = load_input("test_small.txt");
    test_print(test);


    // TODO do the algorithm
    
    return 0;
}