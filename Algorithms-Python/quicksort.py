import time

def quicksort(anArray):
    if len(anArray)<=1:
        return anArray
    # print(anArray)
    pivot = anArray[0]

    left = []
    right = []
    for i in range(1,len(anArray)):
        if anArray[i] < pivot:
            left.append(anArray[i])
        else:
            right.append(anArray[i])

    return quicksort(left) + [pivot] + quicksort(right)


alist = [54,26,93,17,77,31,44,55,20]

for i in range(1000):
    alist.append(i)

start = time.time()
quicksort(alist)
end = time.time()
print("Runtime was: ", (end - start))


# print(quicksort(alist))