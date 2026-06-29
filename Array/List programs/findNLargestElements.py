# Find the N largest elements in the list 
# different methods are discussed in the same program 


# 1. The first method discusses sort method 
def usingSort(arr, n):
    if len(arr) < n :
        return None 
    
    arr.sort()
    return arr[-n:]

# 2. This method uses the sorted function
def usingSorted(arr, n):
    if len(arr) < n :
        return None 
    
    arr = sorted(arr, reverse=True)

    return arr[:n]


print(usingSort([1,2,3,4,5,6,7], 2))
print(usingSorted([-2,-1,4,5,6,7,10,34,12,11,67,87, 32,109, 112, 34, 65], 7))
print(usingSort([], 2))
print(usingSorted([], 2))



# alternatively , there is to explore the heapq as well as the numpy modules
# for the other methods 
# heapq function consists of the nlargest method which is used to obtain the nlargest elements
# then altrnatively we can also use the numpy array, sort it using the argsort() method and 
# perform the same operations as sort 