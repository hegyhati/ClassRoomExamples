
#include <iostream>
#include <string>
using namespace std;


int main() { 
    int state = 0;
    string input;
    cin >> input;
    for (uint idx=0; idx<input.length(); idx++){
        switch(state){
            case 0: switch (input[idx]) {
                case 'a': state = 0; break;
                case 'b': state = 1; break;
                case 'c': state = 0; break;
            } break;
            case 1: switch (input[idx]) {
                case 'a': state = 2; break;
                case 'b': state = 1; break;
                case 'c': state = 0; break;
            } break;
            case 2: switch (input[idx]) {
                case 'a': state = 0; break;
                case 'b': state = 3; break;
                case 'c': state = 0; break;
            } break;
            case 3: switch (input[idx]) {
                case 'a': state = 3; break;
                case 'b': state = 3; break;
                case 'c': state = 3; break;
            } break;

        }
    }
    cout << ( (false  || state==3 )?"Accepted":"Not accepted") << endl;
}
