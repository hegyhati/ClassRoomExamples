from datastructures import PriorityQueue

def swap(l:list[int],idx1:int,idx2:int) -> None:
    l[idx1],l[idx2] = l[idx2],l[idx1]
    
def wasteful_insertion_sort(numbers:list[int]) -> None:  ## O(n^2)
    pq = PriorityQueue(max_queue=False)                  # O(1)
    for number in numbers:                               # O(n) x    -> O(n^2)
        pq.push(number)                                      # O(n)        
    numbers.clear()                                      # O(1)
    while not pq.is_empty():                             # O(n)x     -> O(n)
        numbers.append(pq.pop_max())                         # O(1*) + O(1)


def insertion_sort(numbers:list[int]) -> None:                                     ## O(n^2)
    for sorted in range(1,len(numbers)):                                           # O(n) x 
        current_idx = sorted                                                       #    O(1)
        while current_idx > 0 and numbers[current_idx] < numbers[current_idx-1]:   #    O(n) x
            swap(numbers,current_idx,current_idx-1)                                #        O(1)
            current_idx -= 1                                                       #        O(1)


def bubble_sort(numbers:list[int]) -> None:             ## O(n^2)
    for max in range(len(numbers)-1,1,-1):              # O(n)x
        for idx in range(max):                          #   O(n)x
            if numbers[idx] > numbers[idx+1]:           #     O(1)
                swap(numbers,idx,idx+1)                 #         O(1)

def bubble_sort_tricky(numbers:list[int]) -> None:
    for max in range(len(numbers)-1,1,-1):        
        change = False
        for idx in range(max):                    
            if numbers[idx] > numbers[idx+1]:     
                swap(numbers,idx,idx+1)           
                change = True
        if change == False:
            break

def selection_sort(numbers:list[int]) -> None:           # O(n^2)
    for max in range(len(numbers),1,-1):                # O(n)x
        maxidx = 0                                      #   O(1)
        for i in range(1,max):                          #   O(n)x
            if numbers[i] > numbers[maxidx]:            #     O(1)
                maxidx = i                              #       O(1)
        swap(numbers,maxidx,max-1)                      #   O(1)

def merge_sort(numbers:list[int]) -> None:
    def recursive_merge(numbers:list[int]) -> list[int]: 
        if len(numbers) <= 1: return numbers[:]
        left = recursive_merge(numbers[:len(numbers)//2]) 
        right  = recursive_merge(numbers[len(numbers)//2:])
        return merge(left,right) 

    def merge(sorted1:list[int], sorted2:list[int]) -> list[int]:
        idx1 = idx2 = 0
        if len(sorted1) == 0: return sorted2[:]
        if len(sorted2) == 0: return sorted1[:]
        sorted = []
        while True:
            if sorted1[idx1] < sorted2[idx2]:
                sorted.append(sorted1[idx1])
                idx1 += 1
                if idx1 == len(sorted1):
                    sorted += sorted2[idx2:]
                    break
            else:
                sorted.append(sorted2[idx2])
                idx2 += 1
                if idx2 == len(sorted2):
                    sorted += sorted1[idx1:]
                    break
        return sorted
    
    sorted = recursive_merge(numbers)
    numbers.clear()
    numbers.extend(sorted)

def wasteful_quick_sort(numbers:list[int]) -> None:
    def recursive_quick(numbers:list[int]) -> list[int]:
        if len(numbers) <= 1: return numbers[:]
        pivot = numbers[0]
        left = []
        right = []
        for idx in range(1,len(numbers)):
            if numbers[idx] < pivot:
                left.append(numbers[idx])
            else:
                right.append(numbers[idx])
        left_sorted = recursive_quick(left)
        right_sorted = recursive_quick(right)
        return left_sorted + [pivot] + right_sorted
    
    sorted_numbers = recursive_quick(numbers)
    numbers.clear()
    numbers.extend(sorted_numbers)
    
def quick_sort_lomuto(numbers:list[int], from_idx=0, first_not = None) -> None:
    if first_not is None: first_not = len(numbers)
    if first_not <= from_idx + 1: return
    
    pivot = numbers[from_idx]
    next_idx = from_idx+1
    next_larger_idx = first_not-1
    while next_idx <= next_larger_idx:
        if numbers[next_idx] < pivot:
            next_idx += 1
        else:
            swap(numbers,next_idx,next_larger_idx)
            next_larger_idx -= 1
    swap(numbers,from_idx,next_idx-1)
    
    quick_sort_lomuto(numbers, from_idx, next_idx-1)
    quick_sort_lomuto(numbers, next_idx, first_not)
        
def quick_sort_hoare(numbers:list[int], from_idx=0, first_not = None) -> None:
    if first_not is None: first_not = len(numbers)
    if first_not <= from_idx + 1: return
    
    pivot = numbers[from_idx]
    smaller_idx = from_idx+1
    larger_idx = first_not-1
    
    while True:
        while smaller_idx < first_not and numbers[smaller_idx] < pivot:
            smaller_idx += 1
        while larger_idx > from_idx and numbers[larger_idx] > pivot:
            larger_idx -= 1
        if smaller_idx < larger_idx:
            swap(numbers,smaller_idx,larger_idx)
        else: 
            break
    swap(numbers, from_idx, larger_idx)
    
    quick_sort_hoare(numbers, from_idx, larger_idx)
    quick_sort_hoare(numbers, smaller_idx,first_not)
    
def heap_sort(numbers:list[int]) -> None:
    def left(idx:int) -> int: return 2*idx+1
    def right(idx:int) -> int: return 2*idx+2
    def parent(idx:int) -> int: return (idx-1)//2
    
    def fix(numbers:list[int], idx:int, heapsize:int):
        if left(idx) >= heapsize: return        
        if numbers[idx] > numbers[left(idx)]:
            maxidx = idx
        else:
            maxidx = left(idx)
        if right(idx) < heapsize and numbers[maxidx] < numbers[right(idx)]:
            maxidx = right(idx)
        if maxidx != idx:
            swap(numbers,idx,maxidx)
            fix(numbers, maxidx, heapsize)
    
    def heapify(numbers:list[int]) -> None:
        for idx in range((len(numbers)-1) // 2, -1, -1):
            fix(numbers, idx, len(numbers))
            
    size = len(numbers)
    heapify(numbers)
    while size > 0:
        swap(numbers,0,size-1)
        size -= 1
        fix(numbers, 0,size)

def counting_sort(numbers:list[int], max_number:int|None = None)->None:            ## O(n) + O(max)
    if max_number is None: max_number = max(numbers)                        # O(n)
    count = [0] * (max_number+1)                                            # O(1)
    for number in numbers:                                                  # O(n) x 
        count[number] += 1                                                  #   O(1)
    smaller_count = [0] * (max_number+1)                                    # O(1)
    for number in range(1,max_number+1):                                    # O(max) x
        smaller_count[number] = smaller_count[number-1] + count[number]     #   O(1)
    for number in numbers[:]:                                               # O(n) x
        numbers[smaller_count[number]] = number                             #   O(1)
        smaller_count[number] += 1                                          #   O(1)
    

if __name__ == "__main__":
    import random
    
    test = list(range(20))
    random.shuffle(test)
    print(test)
    counting_sort(test)
    print(test)
            
    
    
