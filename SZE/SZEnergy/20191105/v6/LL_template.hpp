

class LL_Job {  
    struct LLItem{
      Job data;
      LLItem* next;
    };
    
    LLItem* head;


  public:
    LL_Job():head(nullptr){}
    
    void push_back(Job newData){
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

    Job* front(){
      if(head==nullptr) return nullptr;
      else return &(head->data);
    }

    bool empty() const { return head==nullptr; }

    ~LL_Job() {
      while(head!=nullptr)
        pop_front();
    }
};

