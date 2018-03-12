/*
 * Feladat: Kerj be ket pozitiv egesz szamot, ird ki a legkisebb kozos tobbszorosuket.
 * 
 *
 * Peldak:
 * 3 5 -> 15
 * 2 8 -> 8
 * 6 9 -> 18
 *
 */

#include<iostream>
using namespace std;

int lcm1(int a, int b){
    int lcm=1;
    while(lcm%a || lcm%b) lcm++;
    return lcm;
}

int lcm2(int a, int b){
    int lcm=(a>b)?a:b;
    while(lcm%a || lcm%b) lcm++;
    return lcm;
}

int lcm3(int a, int b){
    int max=(a>b)?a:b;
    int lcm=max;
    while(lcm%a || lcm%b) lcm+=max;
    return lcm;
}



int main(){
    int a,b;
    cin >> a >> b;

    

    cout<<"LCM("<<a<<","<<b<<")="<<lcm3(a,b)<<endl;


    return 0;
}

