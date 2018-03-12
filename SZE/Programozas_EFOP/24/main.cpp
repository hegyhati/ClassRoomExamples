/*
 * Feladat: Kerj be egy pozitiv egesz szamot, es ird ki, hogy tizes szamrendszerben hany jegybol all, valamint a szamjegyeinek az osszeget.
 * 
 *
 * Peldak:
 * 123 -> 3
 * 10006 -> 5
 *
 */



#include<iostream>
using namespace std;

int tento(int power){
    int result=1;
    for(int i=0;i<power;i++)
        result*=10;
    return result;
}

int length(int n) {
    int power=1;
    while (n >= tento(power)) power++;
    return power;
}

int length2(int n){
    int power;
    for(power=0;n!=0;n/=10) power++;
    return power;
}

int main(){
    int number;
    cin >> number;

    
    cout << length2(number) << endl;
    
    

    return 0;
}

