#include <iostream>
using namespace std;



int Sherine (int number, int digit) {
    int count = 0;
    if (number/100 == digit) count++;
    if ((number/10)%10 == digit) count++;
    if (number%10 == digit) count++;
    return count;
}

int Christine() {
    int n=1;
    do {
        if(n<1 || n>999) cout<<"Wrong number!"<<endl;
        cin>>n;
    } while (n<1 || n>999);
    return n;
}

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
