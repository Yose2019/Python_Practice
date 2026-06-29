# Given n, which is the size of the sub-list 
# Break the list into sub-lists of size n 
# Essentially the program forms a list of lists  

# 1. The method uses loops and splicing 
def usingLoopsAndSplicing(arr, n):
    lst = []
    i = 0 
    while i < len(arr):
        lst.append(arr[i: i + n])
        i += n 

    return lst

# 2. Using List comprehnsion and range 
def usingListComprehensionAndRange(arr, n):
    lst = [arr[i : i + n] for i in range(0, len(arr), n)] 
    return lst 
 

print(usingLoopsAndSplicing([1,2,3,4,5,6,7,8,9,0], 3))
print(usingListComprehensionAndRange([1,2,3,4,5,6,7,8,9,0], 3))
