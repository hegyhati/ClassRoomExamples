#include <iostream>

using namespace std;

#include "zigzag.h"

int main() {
  zigzag z(3);

  cout << z << " length: " << z.length() << endl;
  z.addPoint(0, 0);
  cout << z << " length: " << z.length() << endl;
  z.addPoint(1, 2);
  cout << z << " length: " << z.length() << endl;
  z.addPoint(3, 4);
  cout << z << " length: " << z.length() << endl;
  z.addPoint(3, 4);
  cout << z << " length: " << z.length() << endl;

  return 0;
}
