mod alloc;

pub struct DynArray {
    size: usize,
    capacity: usize,
    data: *mut u32,
}

impl DynArray {

    pub fn new(capacity: usize) -> Self {
        Self {
            size: 0,
            capacity,
            data: alloc::alloc_u32(capacity),
        }
    }

    pub fn size(&self) -> usize { self.size }

    pub fn at(&self, idx:usize) -> u32 {
        unsafe {*self.data.add(idx)}
    }

    pub fn push_back(&mut self, value: u32) {
        if self.size == self.capacity { self.resize(); }
        unsafe { *self.data.add(self.size) = value; }
        self.size += 1;
    }

    fn resize(&mut self) {
        let new_data = alloc::alloc_u32(self.capacity*2);
        for i in 0..self.size {
            unsafe {*new_data.add(i) = *self.data.add(i);}
        }
        alloc::dealloc_u32(self.data, self.capacity);
        self.data = new_data;
        self.capacity *= 2;
    }
}

impl Drop for DynArray {
    fn drop(&mut self) {
        alloc::dealloc_u32(self.data, self.capacity);
    }
}

impl std::fmt::Display for DynArray {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        write!(f, "[",)?;        
        for i in 0..self.size {
            write!(f, " {}", self.at(i))?;
        }
        write!(f, " + _*{} ]", self.capacity-self.size)
    }
}

fn main() {
    let mut x = DynArray::new(10);
    println!("{}",x);
    x.push_back(1);
    x.push_back(22);
    x.push_back(333);
    println!("{}",x);
    for i in 0..x.size() {
        println!("x[{}] = {}",i,x.at(i));
    }
}