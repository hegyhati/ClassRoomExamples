/*
 * Ask for a number, and print the next two twin primes out
 */

#include <iostream>
using namespace std;


// Mina returns is a number is prime or not
// A bit faster version than the previous one
bool Mina (int n) {
    if (n<2) return false;
    else if (n<4) return true;
    else if (!(n%2)) return false;
    else for (int x=3; x*x<=n; x+=2) if(!(n%x)) return false;
    return true;    
}

// Samer returns if n and n+2 are twin primes
bool Samer (int n) {
    return Mina(n) && Mina(n+2);
}


int main()
{
    int n;
    for(cin>>n;!Samer(n);n++);
    cout<<"The next twin primes are "<<n<<" and "<<n+2<<"."<<endl;
    
    return 0;
}
