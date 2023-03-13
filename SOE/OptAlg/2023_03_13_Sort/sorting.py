from typing import List

def bubble_sort(numbers: List[int]):
    for _ in range(len(numbers)-1):
        for idx in range(len(numbers)-1):
            if numbers[idx] > numbers[idx+1]:
                tmp = numbers[idx]
                numbers[idx] = numbers[idx+1]
                numbers[idx+1] = tmp
    

def bubble2_sort(numbers: List[int]):
    for iteration in range(len(numbers)-1):
        for idx in range(len(numbers)-1-iteration):
            if numbers[idx] > numbers[idx+1]:
                tmp = numbers[idx]
                numbers[idx] = numbers[idx+1]
                numbers[idx+1] = tmp

def insertion_sort(numbers: List[int]):
    unsorted = numbers[::-1]
    numbers.clear()
    for number in unsorted:
        for idx in range(len(numbers)):
            if number < numbers[idx]:
                numbers.insert(idx,number)
                break
        else:
            numbers.append(number)

def insertion2_sort(numbers: List[int]):
    unsorted = numbers[::]
    numbers.clear()
    for number in unsorted:
        if len(numbers) == 0 or number > numbers[-1]:
            numbers.append(number)
        else:
            for idx in range(len(numbers)):
                if number < numbers[idx]:
                    numbers.insert(idx,number)
                    break
        

def insertion_inplace_sort(numbers: List[int]):
    for j in range(1,len(numbers)):
        current=numbers[j]
        while j >= 0:
            j -= 1
            if numbers[j] < current: break
            numbers[j+1]=numbers[j]
        numbers[j+1]=current


def merge(left: List[int], right: List[int]):
    merged = []
    while len(left) > 0 and len(right) > 0:
        min_left = left[0]
        min_right = right[0]
        if min_left < min_right:
            merged.append(min_left)
            left.pop(0)
        else:
            merged.append(min_right)
            right.pop(0)
    merged.extend(left)
    merged.extend(right)
    return merged

def merge2(left: List[int], right: List[int]):
    merged = []
    min_left = left.pop(0)
    min_right = right.pop(0)
    try:
        while True:
            if min_left < min_right:
                merged.append(min_left)
                min_left = left.pop(0)
            else:
                merged.append(min_right)
                min_right=right.pop(0)
    except IndexError:
        if len(left) == 0:
            merged.append(min_right)
            merged.extend(right)
        else:
            merged.append(min_left)
            merged.extend(left)
    return merged


def merge_sort(numbers: List[int]):
    number_lists = [ [number] for number in numbers ]
    while len(number_lists) > 1:
        next_lists = []
        for idx in range(0,len(number_lists)-1,2):
            next_lists.append(merge(number_lists[idx], number_lists[idx+1]))
        if len(number_lists) % 2 == 1:
            next_lists.append(number_lists[-1])
        number_lists = next_lists
    numbers.clear()
    numbers.extend(number_lists[0])

def quick_sort(numbers: List[int]):
    numbers.sort()