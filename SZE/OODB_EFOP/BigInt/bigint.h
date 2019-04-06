#ifndef BIGINT_H
#define BIGINT_H

#include <string>
#include <vector>

#define BASE 100

class BigInt {
  std::vector<unsigned int> digits;
  unsigned int normalize(unsigned int idx);
  void normalize();
  void cropleadingzeros();

public:
  BigInt(unsigned int number = 0);
  // BigInt(std::string number);

  BigInt operator+(const BigInt &other) const;
  // BigInt operator-(const BigInt &other) const;
  // BigInt operator*(const BigInt &other) const;
  // BigInt operator/(const BigInt &other) const;
  // BigInt operator%(const BigInt &other) const;
  BigInt &operator++();
  BigInt &operator--();
  BigInt &operator+=(const BigInt &other);
  // BigInt &operator-=(const BigInt &other);
  // BigInt &operator*=(const BigInt &other);
  // BigInt &operator/=(const BigInt &other);
  // BigInt &operator%=(const BigInt &other);

  bool operator==(const BigInt &other) const;
  bool operator<=(const BigInt &other) const;
  bool operator>=(const BigInt &other) const;
  bool operator!=(const BigInt &other) const;
  bool operator<(const BigInt &other) const;
  bool operator>(const BigInt &other) const;

  std::string toString() const;
};

std::ostream &operator<<(std::ostream &s, const BigInt &number);
// std::istream &operator>>(std::istream &s, BigInt &number);

#endif // BIGINT_H
