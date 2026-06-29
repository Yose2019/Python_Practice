# find the even elements in the list 
# different methods are discussed in the same program 

# 1. Using list comprehension 
def usingListComprehension(arr):
    return list(x for x in arr if x % 2 == 0)

# 2. By looping over the list 
def usingLoops(arr):
    lst = []
    for i in arr:
        if i % 2 == 0:
            lst.append(i)

    return lst 

# 3. This is a method which uses bitwise AND operation 
# Now we need to perform bitwise AND operation for each element
# in this, we need to understand the binary representation of the elements
# the even numbers always end wit 0 and odd ones end with 1
# on performing bitwise AND with 1, the end result depends on whether the number is even or odd
def usingBitwiseAND(arr):
    lst = [x for x in arr if x & 1 == 0]
    return lst 

# 4. The next method is lambda function and filter 
# The syntax of lambda function is that - 
# lambda argument : syntax 
#  filter uses filter(function, iterable)
def usingLambda(arr):
    return list(filter(lambda x : x % 2 == 0 , arr))

print(usingListComprehension([2,5,3,4,7,8,9]))
print(usingLoops([2,5,3,4,7,8,9]))
print(usingBitwiseAND([2,5,3,4,7,8,9]))
print(usingLambda([2,5,3,4,7,8,9]))