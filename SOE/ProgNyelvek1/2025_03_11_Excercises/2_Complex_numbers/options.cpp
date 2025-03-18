// option 1
Complex& Complex::operator += ( double r ) { return *this = *this + r; }
Complex Complex::operator + ( double r ) const {
    return Complex( _real + r, _imag);
} 

// option 2
Complex& Complex::operator += ( double r ) {
    _real += r;
    return *this;
};
Complex Complex::operator + ( double r ) const {return Complex(*this)+=r; }

//option 3
Complex& Complex::operator += ( double r ) {
    _real += r;
    return *this;
};
Complex Complex::operator + ( double r ) const {
    return Complex( _real + r, _imag);
} 