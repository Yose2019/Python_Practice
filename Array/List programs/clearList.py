# the given program explains how to clear a list using different methods 
# clear indicates removing all elements 
# all methods are discussed in the same program 


# 1. Using the clear methods on the list
def clearUsingFunction(arr):
    arr.clear()
    return arr

# 2. Using the del option 
# del value - i.e. del arr[index] deletes the element 
def clearUsingDel(arr):
    del arr[:]
    return arr 

# 3. Using the pop method by traversing over all the entire array 
def clearUsingPop(arr):
    n = len(arr)
    for i in range(n):
        arr.pop() 
    
    return arr 

# 4. the next method is using the remove the index using remove method
def clearUsingRemove(arr):
    n = len(arr)
    for i in range((n - 1), -1, -1):
        arr.remove(arr[i])

    return arr 

# 5. Using reassignment 
def clearUsingReassignment(arr):
    arr = []
    return arr 

print(clearUsingFunction([1,2,3,4,5]))
print(clearUsingPop([1,2,3,4,5]))
print(clearUsingDel([1,2,3,4,5]))
print(clearUsingRemove([1,2,3,4,5]))
print(clearUsingReassignment([1,2,3,4,5]))