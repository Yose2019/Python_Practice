# the program identifies empty lists from lists
# The take-away from this program is that empty lists are treated as boolean false 
# Different methods are discussed in the same program 


# 1. The method uses list comprehension
def usingListComprehension(arr):
    lst = [x for x in arr if x]
    return lst 

# 2. The method uses loops in lists 
def usingLoops(arr):
    lst = []
    for x in lst:
        if x:
            lst.append(x)
    
    return lst 

# 3. The method uses lambda function
def usingLambda(arr):
    lst = list(filter(lambda x : x, arr))
    return lst 

print(usingListComprehension([[1, 2], [], [3, 4], [], [5]]))
print(usingListComprehension([[1, 2], [], [3, 4], [], [5]]))
print(usingListComprehension([[1, 2], [], [3, 4], [], [5]]))
