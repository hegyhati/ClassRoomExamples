#ifndef PRIORITY_QUEUE
#define PRIORITY_QUEUE
#include <iostream>
using std::cerr;

#include <vector>

class PriorityQueue {

    std::vector<int> numbers;

    public:

    PriorityQueue() : numbers() {}

    void push(int num) {
        for(auto it = numbers.begin(); it != numbers.end(); ++it)
            if (*it > num) {
                numbers.insert(it,num);
                return;
            }
        numbers.push_back(num);
    }

    void foo() {
        // c style
        for(unsigned int i = 0; i<numbers.size(); ++i)
            cerr << " " << numbers[i];
        cerr << "\n\n";

        // C++98 style
        for(std::vector<int>::iterator it = numbers.begin(); it != numbers.end(); ++it)
            cerr << " " << *it;
        cerr << "\n\n";

        // C++98 iteration in C++11 style
        for(auto it = numbers.begin(); it != numbers.end(); ++it)
            cerr << " " << *it;
        cerr << "\n\n";

        // C++11 style
        for (const auto& a: numbers) 
            cerr << " " << a;
        cerr << "\n\n";

    }

    int popmax() {
        int tmp = numbers.back();
        numbers.pop_back();
        return tmp;
    }
};

#endif