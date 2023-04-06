#include <iostream>
using namespace std;

#define SIZE 8

class Array {
    int data[SIZE];
    int dataLength;
public:
    Array() : dataLength(0) {
        for (int i=0; i<SIZE; ++i)
            data[i] = 0;
    }

    bool append(int number) {
        if (dataLength==SIZE) return false;
        data[dataLength++] = number;
        return true;
    }

    int& operator[] (int idx) {
        return data[idx];
        //todo no idx check
    }

    bool pop(int idx) {
        if (idx < 0 || idx >= dataLength) return false;
        for(int i=idx+1; i<dataLength; ++i) 
            data[i-1] = data[i];
        data[dataLength--]=0;
        return true;
    }

    bool has(int number) const {
        for (int i=0; i<dataLength; ++i)
            if(data[i]==number) return true;
        return false;
    }

    int count(int number) const {
        int count = 0;
        for (int i=0; i<dataLength; ++i)
            if(data[i]==number) ++count;
        return count;
    }

    int length() const {
        return dataLength;
    }
};

int main(){
    Array myArray;
    int x;
    do {
        cin >> x;
        myArray.append(x);
    } while (x!=0);

    for (int i=0; i<myArray.length(); ++i)
        cout<< myArray[i] << endl;
    
    return 0; 
}