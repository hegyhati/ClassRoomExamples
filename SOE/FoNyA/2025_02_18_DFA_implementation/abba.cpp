#include <iostream>
#include <string>
#include <array>

int main() {
    std::array< std::array<int,4>, 5 > delta = {{
        {1,0,0,0},
        {1,2,0,0},
        {1,3,0,0},
        {4,0,0,0},
        {4,4,4,4}
    }};

    std::string input;
    std::cin >> input;
    unsigned int state = 0;

    for (unsigned int idx = 0; idx < input.length(); idx++) 
        state = delta[state][input[idx]-'a'];
    
    std::cout << (state == 4 ? "Van" : "Nincs") << " benne abba." << std::endl;

}