# This program gives two lists and tells us to remove
# the elements of one list from another list
# different methods which can be used is discussed in the same program 

# 1. using for loop and new list created
def usingLoop(arr, remove):
    lst = []
    for i in arr:
        if i not in remove:
            lst.append(i)

    return lst 

# 2. Using for loop and removing from original
def usingLoopAndRemove(arr, remove):
    for i in remove:
        while i in arr:
            arr.remove(i)

    return arr 

# 3. Using list comprehension
def usingListComprehension(arr, remove):
    arr = [x for x in arr if x not in remove]
    return arr 

# 4. Using Lambda 
def usingLambda(arr, remove):
    lst = list(filter(lambda x : x not in remove, arr))
    return lst 

print(usingLoop([10,10,20,20,30,40,50,60,60], [10,20,40]))
print(usingListComprehension([10,10,20,20,30,40,50,60,60], [10,20,40]))
print(usingLoopAndRemove([10,10,20,20,30,40,50,60,60], [10,20,40]))
print(usingLambda([10,10,20,20,30,40,50,60,60], [10,20,40]))