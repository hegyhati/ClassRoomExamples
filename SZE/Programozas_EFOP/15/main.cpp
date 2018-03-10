/*
 * Feladat: Kerj be egy pozitiv egesz szamot, es ird ki a primtenyezos felbontasat.
 * 
 *
 * Peldak:
 * 7 --> 7
 * 6 --> 2 * 3 
 * 45 --> 3^2 * 5 
 * 1 --> 1 
 * 1024 --> 2^10 
 *
 */



#include<iostream>
using namespace std;

void factorization(int n) {
    while (n!=1){
        int divider;
        for(divider=2;n%divider;divider++);
        cout<<divider;
        n/=divider;
        if(n!=1) cout << " * ";
    }
    cout<<endl;
}

void factorization2(int n) {
    int divider=2;
    while (n!=1){        
        while(n%divider) divider++;
        cout<<divider;
        n/=divider;
        if(n!=1) cout << " * ";
    }
    cout<<endl;
}

void factorization3(int n) {
    int divider=2;
    while (n!=1){        
        while(n%divider) divider++;
        
        while(!(n%divider)){
            cout<<divider;
            n/=divider;
            if(n!=1) cout << " * ";
        }        
    }
    cout<<endl;
}

void factorization4(int n) {
    int divider=2;
    while (n!=1){        
        while(n%divider) divider++;

        cout<<divider;
        int count=0;
        while(!(n%divider)){            
            n/=divider;
            count++;
        }
        if (count!=1) cout<<"^"<<count;        
        if(n!=1) cout << " * ";       
    }
    cout<<endl;
}

int main(){
    int n;
    cin >> n;

    factorization(n);
    factorization2(n);
    factorization3(n);
    factorization4(n);
    
    return 0;
}

