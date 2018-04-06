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

int lengthanddigitsum(int n, int& digitsum){
    int power;
    digitsum=0;
    for(power=0;n!=0;n/=10) {
        digitsum += n%10;
        power++;
    }
    return power;
}

struct lads {
    int length;
    int digitsum;
};

struct lads lengthanddigitsum2(int n){
    struct lads toReturn;
    toReturn.digitsum=0;
    for(toReturn.length=0;n!=0;n/=10) {
        toReturn.digitsum += n%10;
        toReturn.length++;
    }
    return toReturn;
}

int main(){
    int number;
    cin >> number;

    int digitsum=0;

    
    cout << lengthanddigitsum(number,digitsum) << endl;
    cout << digitsum << endl;

    struct lads x;
    x=lengthanddigitsum2(number);
    cout<<x.length<<endl<<x.digitsum<<endl;
    

    return 0;
}

