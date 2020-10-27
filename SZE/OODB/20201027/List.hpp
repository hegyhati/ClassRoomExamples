#ifndef LIST_HPP
#define LIST_HPP



template <typename Foo>
struct ListItem {
    Foo data;
    ListItem<Foo>* next;
}; 

template<typename Foo>
class List {
    public:
        List();
        void put(Foo data);
        bool remove(int position);
        int size() const ;
        Foo getElement(int position) const ;
        void clean();

    private:
        ListItem<Foo>* head;

        bool isGoodPosition(int position) const;
        ListItem<Foo>* getListItem(int position) const ;
};

template<typename Foo>
List<Foo>::List() : head(nullptr) {}

template<typename Foo>
void List<Foo>::put(Foo data) {
    ListItem<Foo>* new_data = new ListItem<Foo>{data,nullptr};
    if (head == nullptr) head=new_data;
    else {        
        ListItem<Foo>* tmp = head;
        while(tmp->next!=nullptr) tmp=tmp->next;
        tmp->next = new_data;
    }
}

template<typename Foo>
bool List<Foo>::remove(int position) {
    if (!isGoodPosition(position)) return false;
    else {
        if(position==0) {
            ListItem<Foo>* tmp=head->next->next;
            delete head;
            head=tmp;

        }
        else {
            ListItem<Foo>* tmp = getListItem(position-1);
            ListItem<Foo>* tmpnn=tmp->next->next;
            delete tmp->next;
            tmp->next = tmpnn;
        }
        return true;
    }
}

template<typename Foo>
int List<Foo>::size() const {
    int size=0;    
    for(ListItem<Foo>* tmp = head; tmp!=nullptr; tmp=tmp->next)  ++ size;
    return size;
}

template<typename Foo>
Foo List<Foo>::getElement(int position) const {
    if (getListItem(position)==nullptr) return Foo();
    return getListItem(position)->data;
}

template<typename Foo>
void List<Foo>::clean(){
    while(size() > 0)
        remove(0);
}

template<typename Foo>
bool List<Foo>::isGoodPosition(int position) const {
    return position >= 0 && position < size();
}

template<typename Foo>
ListItem<Foo>* List<Foo>::getListItem(int position) const {
    if (!isGoodPosition(position)) return nullptr;
    ListItem<Foo>* tmp = head;
    for(int i=0; i<position; i++) tmp=tmp->next;
    return tmp;
}


#endif
