#include "Turtle.hpp"
#include <cmath>

#include <iostream>
#include <string>


using namespace std;

double Turtle::rad(double degree){
  return M_PI*degree / 180;
}

Turtle::Turtle() :x(0),y(0),alpha(90) {}

double Turtle::svgX() {return x+50;}
double Turtle::svgY() {return 50-y;}

void Turtle::fd(double distance) {
  image<<"\t<line x1='"<<svgX()<<"' y1='"<<svgY()<<"'";
  x+=distance*cos(rad(alpha));
  y+=distance*sin(rad(alpha));
  image<<" x2='"<<svgX()<<"' y2='"<<svgY()<<"' style='stroke:rgb(255,0,0);stroke-width:2' />"<<endl;
  
}

void Turtle::lt(double degrees) { rt(-degrees);}
void Turtle::rt(double degrees) { alpha -= degrees;}

double Turtle::getX() const {return x;}
double Turtle::getY() const {return y;}
double Turtle::getAlpha() const {return alpha;}


void Turtle::interpreter(char* filename){
  string command;
  double parameter;  
  image.open(filename,ios::out);
  image << "<svg height='100' width='100'>" << endl;
  do {
    cout<<"Turtle: ("<<x<<","<<y<<") "<<alpha<<endl;
    cin>>command;
    if(command == "quit") { cout << "Goodbye!" <<endl;
    } else if (command == "fd") {
      cin>>parameter; fd(parameter);
    } else if (command == "lt") {
      cin>>parameter; lt(parameter);
    } else if (command == "rt") {
      cin>>parameter; rt(parameter);
    }      
  } while (command != "quit");
  image << "</svg>" << endl;
  image.close();
}
