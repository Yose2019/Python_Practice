# the program is used to identify all the elements with duplicates in them
# Different methods are discussed in the same program 

# 1. Using dictionaries 
def usingDictionaries(arr):
    dct = {}
    for i in arr:
        dct[i] = dct.get(i, 0) + 1

    lst = [x for x, count in dct.items() if count > 1]

    return lst 

# 2. Using the counter which creates a dictionary for the given array

from collections import Counter 

def usingCounter(arr):
    dct = Counter(arr)
    s = set(arr)
    lst = []

    for i in s:
        if dct[i] > 1:
            lst.append(i)

    return lst 


print(usingDictionaries([1, 2, 3, 1, 2, 4, 5, 6, 5]))
print(usingCounter([1, 2, 3, 1, 2, 4, 5, 6, 5]))