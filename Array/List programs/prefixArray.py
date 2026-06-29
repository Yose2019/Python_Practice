# The program is used to generate prefix Array 
# This is also called cumulative sum 
# Different methods are discussed in the same program 

# 1. Using loops 
def usingLoops(arr):
    lst = []
    summation = 0
    for i in arr:
        summation += i
        lst.append(summation)

    return lst 

# 2. Using list comprehension 
def usingListComprehension(arr):
    summation = 0
    lst = [sum(arr[:i+1]) for i in range(len(arr))]
    return lst 


# 3. using numpy array with the inbuilt function cumsum
from numpy import cumsum

def usingCumSum(arr):
    lst = cumsum(arr)
    return lst 


print(usingLoops([1,2,3,4,5]))
print(usingListComprehension([1,2,3,4,5]))
print(usingCumSum([1,2,3,4,5]))