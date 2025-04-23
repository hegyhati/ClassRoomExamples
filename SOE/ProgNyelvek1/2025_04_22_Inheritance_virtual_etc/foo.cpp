class A {

};

class B {

};



vector<> ize;
ize.push_back(A())
ize.push_back(B())

SOSEM Fog menni

Ami mehet:

ize.push_back(new A())
ize.push_back(new B())

de ehhez az kell:
c -bol oroklodjon A
C -bol oroklodjon B
vector<C> ize;


MAS SZITU:


A a;
B b;

foobar(a);
foobar(b);


Ket opcio is van:

1) oroklodes C -bol es :
void foobar(C c) {

}

2) template

template<typename VALAMI>
void foobar(VALAMI valami){
    cout << valami.name << endl;
}
