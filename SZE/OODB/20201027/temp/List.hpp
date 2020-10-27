#ifndef LIST_HPP
#define LIST_HPP

class Foo {};

struct FooListItem {
    Foo data;
    FooListItem* next;
}; 

class FooList {
    public:
        FooList() : head(nullptr) {}
        void put(Foo data) {
            FooListItem* new_data = new FooListItem{data,nullptr};
            if (head == nullptr) head=new_data;
            else {        
                FooListItem* tmp = head;
                while(tmp->next!=nullptr) tmp=tmp->next;
                tmp->next = new_data;
            }
        }
        bool remove(int position) {
            if (!isGoodPosition(position)) return false;
            else {
                if(position==0) head=head->next;
                else {
                    FooListItem* tmp = getListItem(position-1);
                    tmp->next = tmp->next->next;
                }
                return true;
            }
        }
        int size() const {
            int size=0;    
            for(FooListItem* tmp = head; tmp!=nullptr; tmp=tmp->next)  ++ size;
            return size;
        }
        Foo getElement(int position) const {
            if (getListItem(position)==nullptr) return Foo();
            return getListItem(position)->data;
        }

    private:
        FooListItem* head;

        bool isGoodPosition(int position) const {
            return position >= 0 && position < size();
        }
        FooListItem* getListItem(int position) const {
            if (!isGoodPosition(position)) return nullptr;
            FooListItem* tmp = head;
            for(int i=0; i<position; i++) tmp=tmp->next;
            return tmp;
        }
};

#endif
