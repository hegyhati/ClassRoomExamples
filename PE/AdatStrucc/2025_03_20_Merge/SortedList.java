class SortedList{
    class ListItem {
        int value;
        ListItem next;

        public ListItem(int value, ListItem next) {
            this.value = value;
            this.next = next;
        }
    }

    private ListItem head;

    public SortedList() {
        this.head = null;
    }

    public SortedList(SortedList l1, SortedList l2) {
        if (l1.head == null && l2.head == null) {
            this.head = null;
            return;
        }

        ListItem tmp = new ListItem(0,null);
        this.head = tmp;

        while (l1.head != null && l2.head != null) {
            SortedList smaller = l1.head.value < l2.head.value ? l1 : l2;            
            tmp.next = smaller.head;
            tmp = tmp.next;        
            smaller.head = smaller.head.next;
        }

        SortedList nonEmpty = l1.head == null ? l2 : l1;
        tmp.next = nonEmpty.head;
        nonEmpty.head = null;

        this.head = this.head.next;
    }

    public void push(int value) {
        if ( this.head==null || this.head.value > value) {
            this.head = new ListItem(value, this.head);
            return;
        }
        ListItem tmp = this.head;
        while (tmp.next != null && tmp.next.value < value)
            tmp=tmp.next;
        ListItem newItem = new ListItem(value, tmp.next);
        tmp.next = newItem;
    }

    @Override 
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append(System.identityHashCode(this)).append(": ");
        for(ListItem tmp = head; tmp != null; tmp = tmp.next)
            sb.append(tmp.value).append(" (").append(System.identityHashCode(tmp)).append(") -> ");
        return sb.toString();
    }
    
}