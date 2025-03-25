#include <iostream>
#include <vector>
using namespace std;

#include "PriorityQueue.hpp"

int main() {
    PriorityQueue pq;
    
    int num;
    while (true) {
        cin >> num;
        if (num == 0) break;
        pq.push(num);
    }
    
    PriorityQueue pq2 = pq;
    PriorityQueue& pq3 = pq;

    cout << pq.popmax() << endl;
    cout << pq2.popmax() << endl;
    cout << pq3.popmax() << endl;

    pq.foo();
    pq2.foo();
    pq3.foo();



    int a;
    int b{};
    int c(3);
    int d = 3;
    int e{3};

    vector <int> v1;
    vector <int> v2{};
    vector <int> v3(2,3);
    vector <int> v4{2,3,4,5,6,7};




}