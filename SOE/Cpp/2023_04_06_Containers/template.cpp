#include <iostream>
using namespace std;


#define SIZE 16

template <typename T>
class Array {
    T* data;
    int size;
    int dataLength;

    void reallocate(){
        T* newData = new T[size+SIZE];
        cerr << "Reallocating from " << data << " to " << newData << " and increasing the size from " << size << " to " << size + SIZE << ".\n";
        for (int i=0; i<size; ++i)
            newData[i] = data[i];
        delete [] data;
        data = newData; 
        size += SIZE;
    }

public:
    Array(int size = SIZE) : size(size), dataLength(0) {
        data = new T[size];
    }

    ~Array() {
        delete data;
    }


    bool append(T number) {
        if (dataLength==size) reallocate();
        data[dataLength++] = number;
        return true;
    }

    T& operator[] (int idx) {
        return data[idx];
        //todo no idx check
    }

    bool pop(int idx){
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
    int size;
    cin >> size;
    Array<int> myArray(size);
    int x;
    do {
        cin >> x;
        myArray.append(x);
    } while (x!=0);

    for (int i=0; i<myArray.length(); ++i)
        cout<< myArray[i] << endl;
    
    return 0; 
}

