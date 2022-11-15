#include <iostream>
#include <string>

int add(int number1, int number2) {
    return number1+number2;
}

int main() {
    std::string x, y;
    std::cin >> x >> y;
    std::cout << add(x,y);
}