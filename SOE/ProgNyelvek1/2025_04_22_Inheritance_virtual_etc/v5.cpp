#include <iostream>
#include <vector>
#include <string>
using namespace std;


class BeautyRule {
protected:
    const string humanName;
    BeautyRule(string humanName) : humanName(humanName) {}
    virtual bool operator()(const vector<int>& numbers) const = 0; 
public:    
    virtual ~BeautyRule(){}
    bool isSatisfiedWithLogging(const vector<int>& numbers) const {
        cerr << "Testing "<<humanName<<":";
        bool ok = (*this)(numbers);
        cerr << (ok ? "OK" : "NOK" ) << "\n";
        return ok;
    }
};


class ArithmeticSequenceRule : public BeautyRule {
    virtual bool operator()(const vector<int>& numbers) const override {
        if (numbers.size() < 2) return true;
        int diff = numbers[1] - numbers[0];
        for (size_t i = 1; i < numbers.size(); ++i) 
        if (numbers[i] - numbers[i - 1] != diff) 
        return false;
        return true;
    }
public:
    ArithmeticSequenceRule() : BeautyRule("Szamtani sorozat-e") {}
};



class HasPrimeRule : public BeautyRule {
    virtual bool operator()(const vector<int>& numbers) const override {
        for (int num : numbers) 
            if (isPrime(num)) 
                return true;
        return false;
    }
    static bool isPrime(int num) {
        if (num <= 1) return false;
        for (int i = 2; i * i <= num; ++i) {
            if (num % i == 0) return false;
        }
        return true;
    }
public:
    HasPrimeRule() : BeautyRule("Van-e prim szam") {}
};


class NotTooLongRule : public BeautyRule {
    const unsigned int size;
    virtual bool operator()(const vector<int>& numbers) const override {
        return numbers.size() <= size;
    }
public:
    NotTooLongRule(int size) : BeautyRule("Nem tul hosszabb-e mint " + to_string(size)), size(size) {}
};

class BeautyTester { // Considered owner of rule functors
    vector<BeautyRule*> rules;
public:
    ~BeautyTester() {
        for (auto rule: rules) 
            delete rule;
    }
    void addRule(BeautyRule* rule) {
        rules.push_back(rule);
    }
    bool isBeautyful(const vector<int>& numbers) const {
        int count = 0;
        for (auto rule: rules) 
            if(rule->isSatisfiedWithLogging(numbers)) 
                count++;
        return count > 0;
    }
};



int main() {
    vector<int> testNumbers {3,4,5,9};

    BeautyTester tester;
    tester.addRule(new ArithmeticSequenceRule());
    tester.addRule(new HasPrimeRule());
    tester.addRule(new NotTooLongRule(3));
    
    //NotTooLongRule foo(5);
    //tester.addRule(&foo); <-- causes segfault
    
    if (tester.isBeautyful(testNumbers)) 
        cout << "Yaaay, szep szamok!\n";
    else
        cout << ":-( csunya szamok\n";

    return 0;
}

// Ok, no memory leak, but ownership is not expressed by code.