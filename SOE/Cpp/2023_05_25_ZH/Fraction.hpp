#ifndef FRACTION_HPP
#define FRACTION_HPP

#include <numeric>

class Fraction {
    int nominator;
    int denominator;

    void simplify(){
        if (denominator == 0) throw DivisionByZero();

        if (denominator < 0) {
            nominator *= -1;
            denominator *= -1;
        }

        int gcd = std::gcd(nominator,denominator);
        nominator /= gcd;
        denominator /= gcd;
    }

public:
    Fraction(int nominator, int denominator) : nominator(nominator), denominator(denominator) {simplify();}
    Fraction(int integer) : nominator(integer), denominator(1) {}

    struct DivisionByZero{};

    Fraction operator + (const Fraction& other) const {
        return Fraction(nominator * other.denominator + denominator * other.nominator, denominator * other.denominator);
    }

    Fraction operator - (const Fraction& other) const {
        return Fraction(nominator * other.denominator - denominator * other.nominator, denominator * other.denominator);
    }

    Fraction operator * (const Fraction& other) const {
        return Fraction(nominator * other.nominator, denominator * other.denominator);
    }

    Fraction operator / (const Fraction& other) const {
        return Fraction(nominator * other.denominator, denominator * other.nominator);
    }

    void operator += (const Fraction& other) {
        *this = *this + other;
    }

    double real_value() const {
        return (double) nominator / denominator;
    }

    friend std::ostream& operator << (std::ostream& s, const Fraction& f) {
        s << " " << f.nominator;
        if (f.denominator != 1)
            s << "/" << f.denominator;
        return s << " ";
    }
};

#endif // FRACTION_HPP