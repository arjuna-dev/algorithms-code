
# Python program for implementation of Insertion Sort 
  
# Function to do insertion sort 
def insertionSort(arr): 
  
    # Traverse through 1 to len(arr) 
    for i in range(1, len(arr)): 
  
        key = arr[i] 
  
        # Move elements of arr[0..i-1], that are 
        # greater than key, to one position ahead 
        # of their current position 
        j = i-1
        while j >= 0 and key < arr[j] : 
                arr[j + 1] = arr[j] 
                j -= 1
        arr[j + 1] = key 
  
  
# Driver code to test above 
arr = [12, 11, 13, 5, 6, 1] 
insertionSort(arr) 
for i in range(len(arr)): 
    print ("% d" % arr[i]) 
  
# This code is contributed by Mohit Kumra 

#Time complexity
""" 
1. Assign the key
2. Compare 2nd element (key) to the first
3. Instert element in key's place
4. Instert key in element's place
5. Repeat n times iterating one more element each time

For a 6 element array [plus key assignment] [when key is smaller: + placing the key]:
[12, 11, 13, 5, 6, 1]: 1 step comparisson + 1 step swaping
[11, 12, 13, 5, 6, 1]: 0 steps
[11, 12, 13, 5, 6, 1]: 3 steps comparisson + 3 step swaping
[5, 11, 12, 13, 6, 1]: 4 steps comparisson + 3 step swaping
[5, 6, 11, 12, 13, 1]: 5 steps comparisson + 5 step swaping

25 steps (swaping/comparisson)
5 key assignments
4 key plaements

Total = 33 steps

Generalization:

Last iteration: n-1
Second to last: n-2
...
First iteration: 1

So:

(1+2+3+⋯+(n−1))
(n−1+1)((n−1)/2) = n^2/2−n/2
O(n^2)

(4) Consider edge cases - sorted, sorted backwards, all items in the array are the same - how will this affect the time complexity?

Sorted: time complexity O(n). Very good.

Sorted backwards: Very bad, this is the worst case scenario as it will have to reorder every single item.

All items in the array are the same: time complexity O(n). Very good.

Almost sorted: Number of steps would be n + the slot number occupied by the unsorted elements. Not bad.
"""

