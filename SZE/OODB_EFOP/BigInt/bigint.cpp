#include "bigint.h"

unsigned int BigInt::normalize(unsigned int idx) {
  if (digits[idx] < BASE)
    return false;

  unsigned int carry = digits[idx] / BASE;
  digits[idx] %= BASE;
  return carry;
}

void BigInt::normalize() {
  unsigned int carry = 0;
  for (unsigned int idx = 0; idx < digits.size(); ++idx) {
    digits[idx] += carry;
    carry = normalize(idx);
  }
  if (carry != 0)
    digits.push_back(carry);
}

void BigInt::cropleadingzeros() {
  while (digits.back() == 0)
    digits.pop_back();
}

BigInt::BigInt(unsigned int number) {
  digits.push_back(number);
  normalize();
}

BigInt BigInt::operator+(const BigInt &other) const {
  BigInt copy(*this);
  copy += other;
  return copy;
}

BigInt &BigInt::operator++() {
  digits[0]++;
  normalize();
  return *this;
}

BigInt &BigInt::operator--() {
  if (digits.size() != 1 || digits[0] != 0) {
    unsigned int idx = 0;
    while (digits[idx] == 0) {
      digits[idx] = BASE - 1;
      ++idx;
    }
    --digits[idx];
    cropleadingzeros();
  }
  return *this;
}

BigInt &BigInt::operator+=(const BigInt &other) {
  for (unsigned int idx = digits.size(); idx < other.digits.size(); ++idx)
    digits.push_back(0);
  for (unsigned int idx = 0; idx < other.digits.size(); idx++)
    digits[idx] += other.digits[idx];
  normalize();
  return *this;
}

bool BigInt::operator==(const BigInt &other) const {
  if (digits.size() != other.digits.size())
    return false; // TODO felesleges nullak az elejen
  for (unsigned int idx = 0; idx < digits.size(); ++idx)
    if (digits[idx] != other.digits[idx])
      return false;
  return true;
}

bool BigInt::operator<=(const BigInt &other) const { return !(*this > other); }

bool BigInt::operator>=(const BigInt &other) const { return !(*this < other); }

bool BigInt::operator!=(const BigInt &other) const { return !(*this == other); }

bool BigInt::operator<(const BigInt &other) const {
  if (digits.size() < other.digits.size())
    return true;
  else if (digits.size() > other.digits.size())
    return false;
  else {
    for (int idx = digits.size() - 1; idx >= 0; --idx)
      if (digits[idx] < other.digits[idx])
        return true;
      else if (digits[idx] > other.digits[idx])
        return false;
    return false;
  }
}

bool BigInt::operator>(const BigInt &other) const {
  return !(*this < other) && !(*this == other);
}

std::string BigInt::toString() const {
  std::string toReturn = "<";
  for (int idx = digits.size() - 1; idx >= 0; --idx) {
    toReturn += '0' + (digits[idx] / 10);
    toReturn += '0' + (digits[idx] % 10);
    toReturn += ' ';
  }
  toReturn += ">";
  return toReturn;
}

std::ostream &operator<<(std::ostream &s, const BigInt &number) {
  s << number.toString();
  return s;
}
