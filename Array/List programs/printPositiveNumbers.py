# The given program prints the positive numbers in a list 
# all the different approaches are listed in the given program 

from numpy import array
# 1. This method uses a loop and a condition
def usingLoops(arr):
    lst = []
    for i in arr:
        if i >= 0:
            lst.append(i)

    return lst 

# 2. This method uses list comprehension
def usingListComprehension(arr):
    lst = [i for i in arr if i >= 0]
    return lst 

# 3. Using lambda functions 
# This method needs to use a combination of both lambda and the filter 
def usingLambda(arr):
    lst = list(filter(lambda x : x >= 0, arr))
    return lst 

# 4. Using the numpy array
def usingNumpy(arr):
    arr = array(arr)
    arr = arr[arr > 0]
    return arr


print(usingLoops([-1,2,3,4,-2,-9]))
print(usingListComprehension([-3,1,4,5,0]))
print(usingLambda([2,3,4,5,-1,-2,1,2,3]))
print(usingNumpy([-1,-2,3,4,5,9,0]))
