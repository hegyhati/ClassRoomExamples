/*
 * Feladat: Kerj be egy szamot,  majd azt, hogy ez milyen szamrendszerben adott, vegul hogy milyen szamrendszerbe legyen atvaltva
 * Mindket szamrendszerrol feltetelezheto, hogy 2 es 35 kozotti.
 * 
 *
 * Peldak:
 * 3 5 8 -> 3
 * 3 5 2 -> 11
 * 8 10 2-> 1000
 * 11 11 10  -> 12
 * 11 8 10 -> 9
 * F 16 10 -> 15
 * 241 10 16 -> F1
 *
 * 241(10)=F1(16)
 */


#include<iostream>
#include<string>
using namespace std;

int ctoi(char digit){
    if ('0'<=digit && digit <= '9') return digit - '0';
    else return digit -'A' + 10;
}

unsigned long int getValue(string number, int base){
    unsigned long int value=0;
    for (unsigned int x=0; x<number.length(); x++){        
        value *= base;
        value += ctoi(number[x]);
    }
    return value; 
}

char itoc(int value){
    if (value<10) return '0'+value;
    else return 'A'+value-10;
}

string convertToBase(unsigned long int value, int base){
    string number="";
    for(;value!=0;value/=base)
        number = itoc(value%base) + number;
    return number;
}

int main(){
    string numberfrom, numberto;
    int basefrom, baseto;
    cin >> numberfrom >> basefrom >> baseto;
    
    unsigned long int value = getValue(numberfrom, basefrom);
    
    numberto = convertToBase(value, baseto);
    
    cout << numberfrom << "("<<basefrom<<") = " <<numberto <<"("<<baseto<<")\n";


    return 0;
}

