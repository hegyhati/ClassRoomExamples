use std::fmt;

struct Heap {
    data : Vec<i32>
}


#[inline]
fn parent(idx:usize) -> usize { (idx-1)/2 }
#[inline]
fn left(idx:usize) -> usize { 2*idx + 1 }
#[inline]
fn right(idx:usize) -> usize { 2*idx + 2 }

impl Heap {
    fn new() -> Heap {
        Heap { data: vec![] }
    }

    fn push(&mut self, value:i32) {
        let mut new_idx = self.data.len();
        self.data.push(value);
        while new_idx != 0 && self.data[parent(new_idx)] < self.data[new_idx] {
            self.data.swap(new_idx, parent(new_idx));
            new_idx = parent(new_idx);
        }
    }

    fn pop_max(&mut self) -> Option<i32> {
        if self.data.len() <= 1 { return self.data.pop(); }
        else {
            let root = self.data[0];
            let mut moved_idx = 0;
            self.data[moved_idx] = self.data.pop()?;
            loop {
                let mut max_idx = moved_idx;
                if left(moved_idx) < self.data.len() && self.data[left(moved_idx)] > self.data[max_idx] {
                    max_idx = left(moved_idx)
                }
                if right(moved_idx) < self.data.len() && self.data[right(moved_idx)] > self.data[max_idx] {
                    max_idx = right(moved_idx)
                }

                if max_idx == moved_idx { return Some(root); } 
                
                self.data.swap(max_idx, moved_idx);
                moved_idx = max_idx;
            }
        }
    }
}

impl fmt::Display for Heap {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(f, "[")?;
        let mut new_layer_idx = 1;
        for i in 0..self.data.len() {
            if i == new_layer_idx {
                write!(f, "|")?;
                new_layer_idx = left(new_layer_idx);
            }
            write!(f, " {} ", self.data[i])?;
        }
        write!(f, "]")
    }
}

fn main() {
    let mut h:Heap = Heap::new();

    for v in [42, 7, 91, 23, 58, 16, 84, 35, 69, 10] {
        h.push(v);
    }

    println!("{}", h);

    for _ in 0..12 {
        println!("{:?}", h.pop_max());
    }
}