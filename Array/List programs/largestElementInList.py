# This program is used to find the largest element in list 
# different approaches are discussed in the same program 

# 1. This methosd finds the largest element using the max() function 
def largestElementUsingMax(arr):
    return max(arr) 


# 2. This program finds the largest element by travering the array 
def largestElementByTraversing(arr):
    maximum = arr[0] 
    for i in arr:
        if i > maximum:
            maximum = i 

    return maximum 

# 3. This program finds the largest element by sorting and returning the last element 
def largestElementBySort(arr):
    arr.sort()
    return arr[-1]

print(largestElementUsingMax([-1, -10, 1, 3, 5]))
print(largestElementByTraversing([2, 3, 4, 6, 7, 1]))
print(largestElementBySort([-1, -2, -3, -4, -5]))