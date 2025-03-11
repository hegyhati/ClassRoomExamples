
#include "complex.hpp"

Complex::Complex( double real, double imaginary) 
    : _real(real), _imag(imaginary) {}

double Complex::real() const { return _real; }
double Complex::imaginary() const { return _imag; }
Complex Complex::conjugate() const { return Complex( _real,- _imag ); }

Complex Complex::operator - () const { return Complex( - _real, - _imag ); }

Complex Complex::operator + ( double r ) const {return Complex(*this)+=r; }
Complex Complex::operator - ( double r ) const {return Complex(*this)-=r; }
Complex Complex::operator * ( double r ) cs << c.real() onst {return Complex(*this)*=r; }
Complex Complex::operator / ( double r ) const {return Complex(*this)/=r; }

Complex Complex::operator + ( const Complex& c ) const {
    return Complex( _real + c._real , _imag + c._imag );
} 
Complex Complex::operator - ( const Complex& c ) const {
    return Complex( _real - c._real , _imag - c._imag );
} 
Complex Complex::operator * ( const Complex& c ) const {
    return Complex( _real * c._real - _imag * c._imag, _real * c._imag + _imag * c._real );
} 
Complex Complex::operator / ( const Complex& c ) const {
    const double denominator = c._real * c._real +  c._imag * c._imag;
    return (*this) * c.conjugate() / denominator; 
} 

Complex& Complex::operator += ( double r ) {
    _real += r;
    return *this;
};
Complex& Complex::operator -= ( double r ) {
    _real -= r;
    return *this;
}
Complex& Complex::operator *= ( double r ) {
    _real *= r;
    _imag *= r;
    return *this;
}
Complex& Complex::operator /= ( double r ) {
    _real /= r;
    _imag /= r;
    return *this;
}

Complex& Complex::operator += ( const Complex& c ) { return *this = *this + c; }
Complex& Complex::operator -= ( const Complex& c ) { return *this = *this - c; }
Complex& Complex::operator *= ( const Complex& c ) { return *this = *this * c; }
Complex& Complex::operator /= ( const Complex& c ) { return *this = *this / c; }

bool Complex::operator == (const Complex& c ) {
    return _real == c._real && _imag == c._imag;
}

Complex operator + ( double r, const Complex& c ) { return c + r; };
Complex operator - ( double r, const Complex& c ) { return c - r; };
Complex operator * ( double r, const Complex& c ) { return c * r; };
Complex operator / ( double r, const Complex& c ) { return c / r; };

std::ostream& operator << (std::ostream& s, const Complex& c ) {
    if ( c.real() == 0 && c.imaginary() == 0 ) {
        s << "0";
    } else if ( c.real() == 0 ) {
        s << c.imaginary() << "i";
    } else if ( c.imaginary() == 0 ) {
        s << c.real();
    } else {
        s << c.real(); 
        if (c.imaginary() > 0) {
            s << " + " << c.imaginary() << "i";
        } else {
            s << " - " << -c.imaginary() << "i";
        };
    }
    return s;
}