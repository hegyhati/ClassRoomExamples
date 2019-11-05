

class LL {  
    struct LLItem{
      Whatever data;
      LLItem* next;
    };
    
    LLItem* head;


  public:
    LL():head(nullptr){}
    
    void push_back(Whatever newData){
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

    void pop_front(){
      if(head!=nullptr){
        LLItem* tmp=head->next;
        delete head;
        head=tmp;
      }
    }

    Whatever* front(){
      if(head==nullptr) return nullptr;
      else return &(head->data);
    }

    bool empty() const { return head==nullptr; }

    ~LL() {
      while(head!=nullptr)
        pop_front();
    }
};

