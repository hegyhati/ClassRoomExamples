pub fn alloc_u32(count: usize) -> *mut u32 {
    let layout = std::alloc::Layout::array::<u32>(count).unwrap();
    unsafe {std::alloc::alloc(layout) as *mut u32}
}

pub fn dealloc_u32(ptr: *mut u32, count: usize) {
    let layout = std::alloc::Layout::array::<u32>(count).unwrap();
    unsafe {std::alloc::dealloc(ptr as *mut u8, layout)}
}