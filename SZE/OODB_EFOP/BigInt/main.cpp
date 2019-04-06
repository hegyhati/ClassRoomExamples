#include <iostream>

using namespace std;

#include "bigint.h"

int main() {
  BigInt number(105);

  for (int i = 0; i < 15; i++, --number) {
    cout << i << "   " << number.toString() << endl;
  }

  return 0;
}
