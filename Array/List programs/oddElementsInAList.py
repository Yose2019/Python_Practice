# this program discusses about finding the odd elements in the list
# the same thing which is being used in even is used here just with condition for odd 


# 1. Using list comprehension
def usingListComprehension(arr):
    return list(x for x in arr if x % 2 != 0)

# 2. Using loops 
def usingLoops(arr):
    lst = [] 
    for i in arr:
        if i % 2 != 0:
            lst.append(i)
    
    return lst 

# 3. Using the bitwise AND 
def usingBitwiseAND(arr):
    return list(x for x in arr if x & 1 == 1)

# 4. Using the lambda function 
def usingLambda(arr):
    return list(filter(lambda x : x % 2 == 1, arr))

print(usingListComprehension([2,5,3,4,7,8,9]))
print(usingLoops([2,5,3,4,7,8,9]))
print(usingBitwiseAND([2,5,3,4,7,8,9]))
print(usingLambda([2,5,3,4,7,8,9]))
