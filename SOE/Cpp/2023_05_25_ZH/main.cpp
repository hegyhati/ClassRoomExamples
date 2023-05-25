#include <iostream>
#include <vector>
#include "Fraction.hpp"


void simple_test() {
    Fraction half(1,2);
    Fraction third(1,3);
    Fraction threequarter(3,4);
    Fraction eight(8);

    std::cout << half << " + " << third << " = " << (half+third) << std::endl;
    // 1/2 + 1/3 = 5/6
    std::cout << half << " - " << third << " = " << (half-third) << std::endl;
    // 1/2 - 1/3 = 1/6
    std::cout << threequarter << " * " << third << " = " << (threequarter*third) << std::endl;
    // 3/4 * 1/3 = 1/4
    std::cout << threequarter << " * " << eight << " = " << (threequarter*eight) << std::endl;
    // 3/4 * 8 = 6
    std::cout << threequarter << " / " << half << " / " << half << " = " << (threequarter/half/half) << std::endl;
    // 3/4 / 1/2 / 1/2 = 3
}

void leibniz() {
    int n;
    std::cin >> n; 
    std::vector<Fraction> fractions;
    for (int i=0; i < n; ++i)
        fractions.push_back(Fraction( (i%2)?-4:4, 2*i+1) );
    
    for (int p = 1; p<n ; ++p) {
        Fraction sum(0);
        for (int i=0; i<p; ++i) {
            if (i) std::cout << " + ";
            std::cout << fractions[i];
            sum += fractions[i];
        }
        std::cout << " = " << sum.real_value() << std::endl;
    }
}

int main() {
    simple_test();
    leibniz();  
    return 0;  
}