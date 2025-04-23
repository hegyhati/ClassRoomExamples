#include <iostream>
#include <vector>
#include <string>
using namespace std;


class BeautyRule {
public:
    virtual bool isSatisfied(vector<int> numbers) = 0; 
};

class FooRule : public BeautyRule {
    float alma;
}; 

class ArithmeticSequenceRule : public BeautyRule {
public:
    virtual bool isSatisfied(vector<int> numbers) override {
        cerr << "Testing ArithmeticSequenceRule, result:";
        if (numbers.size() < 2) {
            cerr << "true\n";
            return true;
        }
        int diff = numbers[1] - numbers[0];
        for (size_t i = 1; i < numbers.size(); ++i) {
            if (numbers[i] - numbers[i - 1] != diff) {
                cerr << "false" << endl;
                return false;
            }
        }
        cerr << "true\n";
        return true;
    }
};

class BeautyTester {
    vector<BeautyRule*> rules;
public:
    void addRule(BeautyRule* rule) {
        rules.push_back(rule);
    }
    bool isBeautyful(vector<int> numbers) {
        for (auto rule: rules) 
            if(rule->isSatisfied(numbers)) 
                return true;
        return false;
    }
};



int main() {
    vector<int> testNumbers {3,4,5};

    BeautyTester tester;
    tester.addRule(new ArithmeticSequenceRule());

    if (tester.isBeautyful(testNumbers)) 
        cout << "Yaaay, szep szamok!\n";
    else
        cout << ":-( csunya szamok\n";

    return 0;
}