#include <iostream>
#include <vector>

using namespace std;


int main(){
    int size;
    cin >> size;
    std::vector<int> myArray(size);
    int x;
    do {
        cin >> x;
        myArray.push_back(x);
    } while (x!=0);

    for (int i=0; i<myArray.size(); ++i)
        cout<< myArray[i] << endl;
    
    return 0; 
}