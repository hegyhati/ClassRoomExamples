/*
 * Ask for COUNT numbers between MIN and MAX, and print out a histogram of the occurances of the digits.
 * Leading zeros should not be counted
 */

#define COUNT 5
#define MIN 1
#define MAX 999999


#include <iostream>
using namespace std;


// Sharine returns how many times a digit appears in a number (regardless of the size of the number, the only thing that is assumed is that it is a pozitive integer)
int Sherine (int number, int digit) {
    int count = 0;
    while(number!=0){
        if(number%10==digit) count++;
        number /= 10;
    }
    return count;
}

// A bit trickier version doing the same thing (not used, just for illustration)
int Sherine2 (int number, int digit) {
    int count;
    for(count=0;number!=0;number/=10)
        count+=(number%10==digit);
    return count;
}

// Christine asks for an input between 1 and 999, and asks again, if a wrong input is given
// Again, a bit trickier versin than the original
int Christine() {
    int n;
    for(cin>>n ; n<MIN || n>MAX ; cin>>n)
        cout<<"Wrong input, please add a number between "<<MIN<<" and "<<MAX<<"!"<<endl;
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
    int numbers[COUNT];
    for(int x=0;x<COUNT;x++) numbers[x] = Christine();

    int digits[10];
    for(int d=0;d<10;d++) digits[d]=0;

    for(int d=0; d<10; d++)
        for(int x=0; x<COUNT; x++)
            digits[d]+=Sherine(numbers[x],d);
   
    Bassem(digits);
    return 0;
}
