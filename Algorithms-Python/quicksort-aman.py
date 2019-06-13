import time

def quicksort(array):
    if len(array)<=1:
        return array
    
    
    pivot = array[0]
    array.pop(0)

    left = []
    right = []
    for i in array:
        if i < pivot:
            left.append(i)
        else:
            right.append(i)

    return quicksort(left) + [pivot] + quicksort(right)


alist = [54,26,93,17,77,31,44,55,20]

for i in range(1000):
    alist.append(i)

start = time.time()
quicksort(alist)
end = time.time()
print("Runtime was: ", (end - start))

# print(quicksort(alist))