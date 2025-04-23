#include <iostream>
#include <vector>
#include <string>
using namespace std;


class BeautyRule {
public:
    string humanName;
    BeautyRule(string humanName) : humanName(humanName) {}
    
    bool isSatisfiedWithLogging(vector<int> numbers) {
        cerr << "Testing "<<humanName<<":";
        bool ok = isSatisfied(numbers);
        cerr << (ok ? "OK" : "NOK" ) << "\n";
        return ok;
    }
    virtual bool isSatisfied(vector<int> numbers) = 0; 
};


class ArithmeticSequenceRule : public BeautyRule {
public:
    ArithmeticSequenceRule() : BeautyRule("Szamtani sorozat-e") {}
    virtual bool isSatisfied(vector<int> numbers) override {
        if (numbers.size() < 2) return true;
        int diff = numbers[1] - numbers[0];
        for (size_t i = 1; i < numbers.size(); ++i) 
            if (numbers[i] - numbers[i - 1] != diff) 
                return false;
        return true;
    }
};



class HasPrimeRule : public BeautyRule {
public:
    HasPrimeRule() : BeautyRule("Van-e prim szam") {}
    virtual bool isSatisfied(vector<int> numbers) override {
        for (int num : numbers) 
            if (isPrime(num)) 
                return true;
        return false;
    }

private:
    bool isPrime(int num) {
        if (num <= 1) return false;
        for (int i = 2; i * i <= num; ++i) {
            if (num % i == 0) return false;
        }
        return true;
    }
};


class NotTooLongRule : public BeautyRule {
public:
    int size;
    NotTooLongRule(int size) : BeautyRule("Nem tul hosszabb-e mint " + to_string(size)), size(size) {}
    virtual bool isSatisfied(vector<int> numbers) override {
        return numbers.size() <= size;
    }
};

class BeautyTester {
    vector<BeautyRule*> rules;
public:
    void addRule(BeautyRule* rule) {
        rules.push_back(rule);
    }
    bool isBeautyful(vector<int> numbers) {
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

    if (tester.isBeautyful(testNumbers)) 
        cout << "Yaaay, szep szamok!\n";
    else
        cout << ":-( csunya szamok\n";

    return 0;
}