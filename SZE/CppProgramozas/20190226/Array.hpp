template <class T>
class Array {
    unsigned int _size;
    T * data;

    // TODO initialize new values
    void resize (unsigned int newsize) {
      T * tmp = new T [newsize];
      for(unsigned int i=0;i<_size && i<newsize;i++)
        tmp[i]=data[i];
      delete [] data;
      data = tmp;
      _size = newsize;
    }
    
  public:
    Array(unsigned int size=1, T defaultvalue=0)
      : _size(size), data(new T[size]) {
      for(unsigned int i=0; i<_size; i++)
        data[i]=defaultvalue;
    }

    Array(const Array<T>& other)
      : _size(other._size){
        data = new T[_size];
        for(unsigned int i=0;i<_size;i++)
          data[i]=other.at(i);
    }

    void operator=(const Array<T>& other){
      delete [] data;
      _size=other._size;
      data = new T[_size];
      for(unsigned int i=0;i<_size;i++)
        data[i]=other.at(i);
    }

    ~Array(){ delete [] data;}
    
    unsigned int size() const { return _size; }
    
    T& operator[](unsigned int idx) {
      if (idx >= _size) resize(idx+1);
      return data[idx];
    }

    T at(unsigned int idx) const {
      if (idx >= _size) return 0;
      return data[idx];
    }
};

template<class T>
ostream& operator << (ostream& s, const Array<T>& a){
  for(unsigned int i=0;i<a.size();i++)
    s << a.at(i) << " ";
  return s;
}
