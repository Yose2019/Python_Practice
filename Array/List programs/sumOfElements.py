# this program demonstartes how to perform the sum of elements of the list
# all different methods are discussed in the same program 

'''
Note : For the binary search method of finding the array sum with O(logn) time complexity
check the program arraySumDivideAndConquer.py in the same folder 
'''

# 1. Array sum using the sum() function 
def sumUsingFunction(arr):
    return sum(arr)

# 2. By traversing over the list 
def sumUsingTraversing(arr):
    s = 0
    for i in arr:
        s += i 

    return s 

# 3. The third method combines the first and second method 
# we use list comprehension and the sum funcion together 
def sumUsingListComprehension(arr):
    s = sum([i for i in arr])
    return s 

print(sumUsingFunction([1,2,3,4,5]))
print(sumUsingTraversing([1,2,3,4,5]))
print(sumUsingListComprehension([1,2,3,4,5]))