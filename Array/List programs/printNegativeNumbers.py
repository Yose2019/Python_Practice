# The program prints negative numbers in a list 
# different methods are discussed in the same program

from numpy import array

# 1. Using loops 
def usingLoops(arr):
    lst = []
    for i in arr:
        if i < 0:
            lst.append(i)

    return lst 

# 2. Using list comprehension
def usingListComprehension(arr):
    lst = [x for x in arr if x < 0]
    return lst 

# 3. Using lambda function
def usingLambda(arr):
    lst = list(filter(lambda x : x < 0, arr))
    return lst 

# 4. Using Numpy
def usingNumpy(arr):
    arr = array(arr)
    arr = arr[ arr < 0 ]
    return arr

print(usingLoops([-1,2,3,4,-2,-9]))
print(usingListComprehension([-3,1,4,5,0]))
print(usingLambda([2,3,4,5,-1,-2,1,2,3]))
print(usingNumpy([-1,-2,3,4,5,9,0]))