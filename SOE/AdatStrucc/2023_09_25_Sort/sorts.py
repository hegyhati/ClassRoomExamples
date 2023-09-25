

def max_selection_sort(t):
    for i in range(len(t)-1):
        max_idx = 0
        for idx in range(len(t)-i):
            if t[max_idx] < t[idx]:
                max_idx = idx
        t[max_idx],t[-1-i] = t[-1-i], t[max_idx]

def bubble_sort(t):
    for i in range(len(t)-1):
        for j in range(len(t)-1-i):
            if t[j] > t[j+1]:
                t[j],t[j+1] = t[j+1], t[j]

def not_so_clever_bubble_sort(t):
    for i in range(len(t)-1):
        swap = False
        for j in range(len(t)-1-i):
            if t[j] > t[j+1]:
                t[j],t[j+1] = t[j+1], t[j]
                swap = True
        if not swap: return


def not_so_genius_bubble_sort(t):
    prev_last_swap = len(t)-1
    while prev_last_swap != -1:
        last_swap=-1
        for j in range(prev_last_swap):
            if t[j] > t[j+1]:
                t[j],t[j+1] = t[j+1], t[j]
                last_swap=j
        prev_last_swap = last_swap

def lazy_quick_sort(t, start=0, end=None):
    if end == None: end = len(t)-1
    if start >= end: return 
    pivot = t[start]
    tmp = t[start+1:end+1]
    next_smaller_idx = start
    next_larger_idx = end
    for item in tmp:
        if item < pivot: 
            t[next_smaller_idx] = item
            next_smaller_idx += 1
        else:
            t[next_larger_idx] = item
            next_larger_idx -= 1
    t[next_smaller_idx] = pivot
    lazy_quick_sort(t,start,next_larger_idx-1)
    lazy_quick_sort(t,next_larger_idx+1,end)

def quick_sort(t, start=0, end=None):
    if end == None: end = len(t)-1
    if start >= end: return 
    pivot = t[start]
    first_larger_idx = start+1
    last_smaller_idx = end
    while True:
        while (t[first_larger_idx] < pivot):
            first_larger_idx += 1
            if first_larger_idx >= end: 
                t[start],t[end] = t[start],t[end]
                quick_sort(t,start, end-1)
                return
        while (t[last_smaller_idx] > pivot):
            last_smaller_idx -= 1
            if last_smaller_idx == start:
                quick_sort(t,start+1,end)
                return
        if last_smaller_idx < first_larger_idx: break
        t[first_larger_idx],t[last_smaller_idx] = t[last_smaller_idx], t[first_larger_idx]
    t[last_smaller_idx],t[start]=t[start],t[last_smaller_idx]
    quick_sort(t,start,last_smaller_idx-1)
    quick_sort(t,first_larger_idx,end)


if __name__ == "__main__":
    #from random import shuffle
    #test = list(range(1000))
    #shuffle(test)
    test = [5,3,8,2,7,4,9,6]
    print(test)
    quick_sort(test)
    print(test)
