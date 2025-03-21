def insertion_sort(numbers:list[int]):
    for idx in range(1,len(numbers)):
        current = numbers[idx]
        idx2 = idx-1
        while(True):
            if idx2 == -1 or numbers[idx2] < current:
                numbers[idx2+1] = current
                break
            else:
                numbers[idx2+1] = numbers[idx2]
                idx2 -= 1

l = [101,1,56,3,2,76,34]
insertion_sort(l)
print(l)
