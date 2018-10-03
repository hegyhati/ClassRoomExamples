template <class T>
class List{

    struct LItem {
      T data;
      struct LItem* next;
    };

    LItem* head;

    void pop(){
      if(head != NULL) {
        LItem *temp=head;
        head=head->next;
        delete temp;
      }
    }
    
  public:

    List() : head(NULL){}
    ~List() {      
      while(head!=NULL) pop();
    }
    
    void add(T t) {      
      if(head==NULL){
        head=new LItem;
        head->data=t;
        head->next=NULL;
      } else {
        LItem *temp=head;
        while(temp->next != NULL) temp=temp->next;
        temp->next=new LItem;
        temp->next->data=t;
        temp->next->next=NULL;
      }
    }
    
    void printAll() const {      
      for(LItem* temp=head; temp!=NULL; temp=temp->next)
        temp->data.print();
    }
    bool empty() const{
      return (head == NULL);
    }

    int size() const{
      int toReturn=0;
      for(LItem* temp=head;temp!=NULL;temp=temp->next)
        toReturn++;
      return toReturn;
    }

    // Warning: out of index
    T getElement(int index) const {
      LItem* temp;
      for(temp=head;index>0;temp=temp->next) index--;
      return temp->data;
    }
};
