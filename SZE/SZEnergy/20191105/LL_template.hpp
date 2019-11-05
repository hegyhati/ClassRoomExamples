
template <class T>
class LL {  
    struct LLItem{
      T data;
      LLItem* next;
    };
    
    LLItem* head;


  public:
    LL():head(nullptr){}
    
    void push_back(T newData);

    void pop_front();

    T* front();

    bool empty() const { return head==nullptr; }

    ~LL() {
      while(head!=nullptr)
        pop_front();
    }
};

template<class T>
void LL<T>::push_back(T newData){
  if(head==nullptr){
    head  = new LLItem;
    head->data = newData;
    head->next = nullptr;
  } else {
    LLItem* tmp=head;
    while(tmp->next!= nullptr) tmp=tmp->next;
    tmp->next = new LLItem;
    tmp->next->data = newData;
    tmp->next->next = nullptr;
  }
}

template<class T>
void LL<T>::pop_front(){
  if(head!=nullptr){
    LLItem* tmp=head->next;
    delete head;
    head=tmp;
  }
}

template<class T>
T* LL<T>::front(){
  if(head==nullptr) return nullptr;
  else return &(head->data);
}
