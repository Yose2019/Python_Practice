# The program discusses counting the number of unique elements in list 
# If the element whose count is to be known is given , the we can run a loop with an if condition
# Different methods are discussed in the same program 

# 1. Using count and print 
def usingCount(arr):
    for i in set(arr):
        print(i, arr.count(i))

# 2. Using dictionaries
def usingDictionaries(arr):
    count = {}
    for i in arr:
        count.setdefault(i, 0)
        count[i] += 1

    for i, cnt in count.items():
        print([i, cnt], end=" ")

# 3. Instead of creating a dictionary , we can use the counter unction from collections 
# The counter creates a dictionary

from collections import Counter

def usingCounter(arr): 
    b = Counter(arr)
    st = set(arr)
    for i in st:
        print([i,b[i]], end=" ",sep=",")

print(usingCount([1,2,3,4,1,2,3,4,5,6,1,2,3,2,3,4,1,2,3,5,6,4,7,8,1,2,3]))
print(usingCounter([1,2,3,4,1,2,3,4,5,6,1,2,3,2,3,4,1,2,3,5,6,4,7,8,1,2,3]))
print(usingDictionaries([1,2,3,4,1,2,3,4,5,6,1,2,3,2,3,4,1,2,3,5,6,4,7,8,1,2,3]))