#include <iostream>

// 1) Beker ket szam, kiir nagyobb
void feladat_1(){
    int a,b;
    std::cin >> a >> b;
    std::cout << (a>b ? a : b) << '\n';
}

// 2) Ker be szamokat addig, amig novekszik.
void feladat_2(){
    int prev, next;
    std::cin >> next;
    do {
        prev = next;
        std::cin >> next;
    } while (next>prev);
}

// 3) Ker be szamokat 0-ig, kiirja a legnagyobbat.
void feladat_3(){
    int x, max = 0;
    do {
        std::cin >> x;
        if (x>max) max=x;
    } while (x != 0);

    std::cout << max << '\n';
}

// 3b) Kerjen be 8 szamot, irja ki a legnagyobbat.
#define SIZE 8
void feladat_3b(){
    int numbers[SIZE];
    for (int i=0; i<SIZE; ++i) std::cin >> numbers[i];
    int max = numbers[0];
    for (int i=0; i<SIZE; ++i) 
        if (numbers[i]>max)
            max = numbers[i];
    std::cout << max << '\n'; 
}

// 4) Elso x Fibonacci szam
void feladat_4(){
    unsigned int count;
    std::cin >> count;
    int tmp, prev=0, next=1;
    while (count--) {
        std::cout << next << '\n';
        tmp = next;
        next = prev+next;
        prev = tmp;
    }
}

// 5) kerje be n-t, k-t, szamolja ki n alatta k -t.
void feladat_5() {
    unsigned int n,k;
    std::cin >> n >> k;
    unsigned long int result = 1;
    for (unsigned int i=n; i>n-k; --i) result *= i;
    for (unsigned int i=1; i<=k; ++i) result /= i;
    std::cout << result << '\n';
}

int main() {
    feladat_5();
    return 0;
}