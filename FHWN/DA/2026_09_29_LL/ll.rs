struct Node {
    data: u32,
    next: *mut Node,
}

impl Node {
    fn new(data:u32, next: *mut Node) -> *mut Node {
        let layout = std::alloc::Layout::new::<Node>();
        unsafe {
            let ptr : *mut Node = std::alloc::alloc(layout) as *mut Node;
            (*ptr).data = data;
            (*ptr).next = next;
            ptr as *mut Node
        }
    }
}

struct LL {
    head: *mut Node,
}

impl LL {
    pub fn new() -> Self {
        LL { head : std::ptr::null_mut() }
    }

    pub fn size(&self) -> usize {
        let mut current = self.head;
        let mut count = 0;
        while !current.is_null() {
            count += 1;
            unsafe { current = (*current).next; }
        }
        count
    }

    pub fn push_front(&mut self, value:u32) {
        self.head = Node::new(value, self.head);
    }

    pub fn push_back(&mut self, value:u32) {
        if self.head.is_null() {
            self.push_front(value);
        } else {
            unsafe {
                let mut current = self.head;
                while !(*current).next.is_null() {
                    current = (*current).next;
                }
                (*current).next = Node::new(value, std::ptr::null_mut());
            }
        }
    }
}

impl Drop for LL {
    fn drop(&mut self) {
        let layout = std::alloc::Layout::new::<Node>();
        while !self.head.is_null() {
            let tmp = self.head;
            unsafe {
                self.head = (*self.head).next; 
                std::alloc::dealloc(tmp as *mut u8, layout)
            }
        }
    }
}

impl std::fmt::Display for LL {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        let mut current = self.head;        
        write!(f, "HEAD({:p}) -> ", self.head)?;
        unsafe {
            while !current.is_null() {
                write!(f, "[{}, {:p}] -> ", (*current).data, (*current).next)?;
                current = (*current).next;
            }
        } 
        write!(f, "NULL")
    }
}

fn main() {
    let mut ll1 = LL::new();
    ll1.push_front(1);
    ll1.push_front(22);
    ll1.push_front(333);
    ll1.push_back(4444);
    println!("{}", ll1.size());
    println!("{}", ll1);
}