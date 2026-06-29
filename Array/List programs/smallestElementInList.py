# This program helps to find the smallest element in the list 
# different methods are discussed in the same program 

# 1. This method uses the min function 
def smallestElementUsingMin(arr):
    return min(arr) 

# 2. Finding the smallest element by travesing the list 
def smallestElementByTraversing(arr):
    minimum = arr[0] 
    i = 1
    while i < len(arr):
        if arr[i] < minimum:
            minimum = arr[i] 
        i += 1 

    return minimum 

# 3. Finding the smallest element sorting the list and return the first element 
def smallestElementBySorting(arr):
    arr.sort()
    return arr[0] 

print(smallestElementUsingMin([-1, 1, 3, -6, -5]))
print(smallestElementByTraversing([2,4,5,6,0]))
print(smallestElementBySorting([-13, -3, -2, -10, -23, -11, -2]))