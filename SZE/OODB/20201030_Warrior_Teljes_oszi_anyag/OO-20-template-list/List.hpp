#ifndef LIST_HPP
#define LIST_HPP


struct WrongIndexException{int index;};

template<typename T>
class List {
  public:

    List();

    ~List();
    List(const List&)=delete;
    List& operator=(const List&)=delete;

    int count() const;
    bool isEmpty() const;
    const T& get(int index) const;

    void put(const T& data);
    T pop(int index);
    void clear();

  private:

    struct Element {
      T data;
      Element* next;
    };

    Element* head;
    
    void checkIndex(int index) const;
};

template<typename T>
List<T>::List() : head(nullptr) {}

template<typename T>
List<T>::~List() { clear(); }

template<typename T>
int List<T>::count() const {
  int count=0;  
  for(List<T>::Element* tmp=head;tmp!=nullptr; tmp=tmp->next) count++;
  return count;
}

template<typename T>
void List<T>::put(const T& data) {
  head = new List<T>::Element{data,head};
}

template<typename T>
const T& List<T>::get(int index) const {
  checkIndex(index);
  List<T>::Element* tmp;
  for(tmp=head;index>0;--index) tmp=tmp->next;
  return tmp->data;
}

template<typename T>
T List<T>::pop(int index) {
  checkIndex(index);
  List<T>::Element** tmp;
  for(tmp=&head;index>0;--index) tmp=&((*tmp)->next);
  T toReturn = (*tmp)->data;
  List<T>::Element* toDelete=(*tmp);
  (*tmp) = (*tmp)->next;
  delete toDelete;
  return toReturn;
}

template<typename T>
void List<T>::clear(){
  while(count()>0) pop(0);
}

template<typename T>
void List<T>::checkIndex(int index) const {
  if (index<0 || index>=count()) throw WrongIndexException{index};
}

#endif
