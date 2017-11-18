/*
 * Ask for 5 numbers between 1 and 999, and print out a histogram of the occurances of the digits.
 * If a number is less then 3 digits long, the leading zeros should be counted.
 */

#include <iostream>
using namespace std;


// Sharine returns how many times a digit appears in a number
int Sherine (int number, int digit) {
    int count = 0;
    if (number/100 == digit) count++;
    if ((number/10)%10 == digit) count++;
    if (number%10 == digit) count++;
    return count;
}

// Christine asks for an input between 1 and 999, and asks again, if a wrong input is given
int Christine() {
    int n=
    do {
        cin>>n;
    } while (n<1 || n>999);
    return n;
}

// Bassem prints out the histogram of the digit array
void Bassem(int occurances[]) {
    for(int d=0; d<10; d++) {
        cout << d << "|";
        for(int x=0;x<occurances[d];x++) cout<<"#";
        cout << endl;
    }
}


int main()
{
    int numbers[5];
    for(int x=0;x<5;x++) numbers[x] = Christine();

    int digits[10];
    for(int d=0;d<10;d++) digits[d]=0;

    for(int d=0; d<10; d++)
        for(int x=0; x<5; x++)
            digits[d]+=Sherine(numbers[x],d);
   
    Bassem(digits);
    return 0;
}
