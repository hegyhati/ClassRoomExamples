#include <iostream>
using namespace std;

class intArray {
    unsigned int _size;
    int * data;

    // TODO initialize new values
    void resize (unsigned int newsize) {
      int * tmp = new int [newsize];
      for(unsigned int i=0;i<_size && i<newsize;i++)
        tmp[i]=data[i];
      delete [] data;
      data = tmp;
      _size = newsize;
    }
    
  public:
    intArray(unsigned int size=1, int defaultvalue=0)
      : _size(size), data(new int[size]) {
      for(unsigned int i=0; i<_size; i++)
        data[i]=defaultvalue;
    }

    intArray(const intArray& other)
      : _size(other._size){
        data = new int[_size];
        for(unsigned int i=0;i<_size;i++)
          data[i]=other.at(i);
    }

    void operator=(const intArray& other){
      delete [] data;
      _size=other._size;
      data = new int[_size];
      for(unsigned int i=0;i<_size;i++)
        data[i]=other.at(i);
    }

    ~intArray(){ delete [] data;}
    
    unsigned int size() const { return _size; }
    
    int& operator[](unsigned int idx) {
      if (idx >= _size) resize(idx+1);
      return data[idx];
    }

    int at(unsigned int idx) const {
      if (idx >= _size) return 0;
      return data[idx];
    }
};

ostream& operator << (ostream& s, const intArray& a){
  for(unsigned int i=0;i<a.size();i++)
    s << a.at(i) << " ";
  return s;
}




class doubleArray {
    unsigned int _size;
    double * data;

    // TODO initialize new values
    void resize (unsigned int newsize) {
      double * tmp = new double [newsize];
      for(unsigned int i=0;i<_size && i<newsize;i++)
        tmp[i]=data[i];
      delete [] data;
      data = tmp;
      _size = newsize;
    }
    
  public:
    doubleArray(unsigned int size=1, double defaultvalue=0)
      : _size(size), data(new double[size]) {
      for(unsigned int i=0; i<_size; i++)
        data[i]=defaultvalue;
    }

    doubleArray(const doubleArray& other)
      : _size(other._size){
        data = new double[_size];
        for(unsigned int i=0;i<_size;i++)
          data[i]=other.at(i);
    }

    void operator=(const doubleArray& other){
      delete [] data;
      _size=other._size;
      data = new double[_size];
      for(unsigned int i=0;i<_size;i++)
        data[i]=other.at(i);
    }

    ~doubleArray(){ delete [] data;}
    
    unsigned int size() const { return _size; }
    
    double& operator[](unsigned int idx) {
      if (idx >= _size) resize(idx+1);
      return data[idx];
    }

    double at(unsigned int idx) const {
      if (idx >= _size) return 0;
      return data[idx];
    }
};

ostream& operator << (ostream& s, const doubleArray& a){
  for(unsigned int i=0;i<a.size();i++)
    s << a.at(i) << " ";
  return s;
}
int main() {

  intArray tomb(13);
  
  cout << tomb << endl;
  tomb[6]=4234234;
  cout << tomb << endl;

  cout << tomb[8] << endl;

  intArray tomb2 = tomb;
  intArray tomb3(tomb);
  intArray tomb4;
  tomb4 = tomb;


  
  tomb[1]=111;
  tomb2[2]=222;
  tomb3[3]=333;
  tomb4[4]=444;

  cout << "tomb" << tomb << endl;
  cout << "tomb2" << tomb2 << endl;
  cout << "tomb3" << tomb3 << endl;
  cout << "tomb4" << tomb4 << endl;

  doubleArray dtomb;
  dtomb[32]=1.23654;
  cout << dtomb << endl;
  
}
