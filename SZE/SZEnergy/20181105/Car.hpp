#ifndef CAR_HPP
#define CAR_HPP

class Car{
    double x;
    double y;
    double alpha;
    double v;
    double a;
  public:  
    Car(double s0=0, double v0=0, double a=0);
    Car(double x, double y, double alpha, double v0, double a=0);
      
    void elapseTime(double t);
    
    double getDist() const;
};

#endif
