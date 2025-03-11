#ifndef COMPLEX_HPP
#define COMPLEX_HPP

#include <iostream>

class Complex {
        double _real;
        double _imag;

    public:
        Complex( double real = 0, double imaginary = 0);
        
        double real() const;
        double imaginary() const;
        Complex conjugate() const;
        
        
        Complex operator - () const;
        
        Complex operator + ( double r ) const;
        Complex operator - ( double r ) const;
        Complex operator * ( double r ) const;
        Complex operator / ( double r ) const;

        Complex operator + ( const Complex& c ) const;
        Complex operator - ( const Complex& c ) const;
        Complex operator * ( const Complex& c ) const;
        Complex operator / ( const Complex& c ) const;

        Complex& operator += ( double r );
        Complex& operator -= ( double r );
        Complex& operator *= ( double r );
        Complex& operator /= ( double r );

        Complex& operator += ( const Complex& c );
        Complex& operator -= ( const Complex& c );
        Complex& operator *= ( const Complex& c );
        Complex& operator /= ( const Complex& c );

        bool operator == (const Complex& c );
};


Complex operator + ( double r, const Complex& c ) ;
Complex operator - ( double r, const Complex& c ) ;
Complex operator * ( double r, const Complex& c ) ;
Complex operator / ( double r, const Complex& c ) ;


std::ostream& operator << (std::ostream& s, const Complex& c );

#endif