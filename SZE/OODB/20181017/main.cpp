#include <iostream>
using namespace std;

class Vector2D {
  private:
    double x;
    double y;
  public:
    Vector2D()
      :x(0),y(0){ cerr<<"default"<<endl;}
    Vector2D(double x, double y)
      :x(x),y(y){cerr<<"x-y konstruktor"<<endl;}
    Vector2D(const Vector2D& other)
      :x(other.x),y(other.y){cerr<<"copy"<<endl;}
    double getX() const {return x;}
    double getY() const {return y;}

    double operator* (const Vector2D& masik) const {
      return x*masik.x+y*masik.y;
    }

    Vector2D operator *(double szorzo) const {
        return Vector2D(x*2,y*2);
    }

    
};

Vector2D operator+ (const Vector2D& egyik, const Vector2D& masik) {
  return Vector2D(egyik.getX()+masik.getX(),egyik.getY()+masik.getY());
}

Vector2D operator *(double szorzo, const Vector2D& vektor){
  return vektor*szorzo;
}

ostream& operator <<(ostream& stream, const Vector2D& vektor){
  stream<<"("<<vektor.getX()<<","<<vektor.getY()<<")";
  return stream;
}



int main(){
  Vector2D v1(2,3);
  Vector2D v2(0,-1); 

  Vector2D v3 = v1 + v2;

  cout<<"v1: "<<v1<<endl;
  cout<<"v2: "<<v2<<endl;
  cout<<"v3=v1+v2: "<<v3<<endl;
  cout<<"v1*v2: "<< v1*v2 <<endl;
  cout<<"v1*2: "<< v1*2 <<endl;
  cout<<"3*v1: "<<3*v1<<endl;

  
}




