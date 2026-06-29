# this program discusses different methods for reversing a list 
# all the methods are discussed in the same program 

# 1. This method discusses the reversing of the list by swapping the elements 
def reverseUsingSwap(arr):
    i, j = 0, len(arr) - 1 

    while i <= j:
        arr[i], arr[j] = arr[j], arr[i] 
        i += 1; j -= 1; 

    return arr 

# 2. Uisng the slicing method with the skip in opposite direction 
def reverseUsingSlice(arr):
    arr = arr[::-1]
    return arr 

# 3. Using the reverse method - arr.reverse() 
def reverseUsingReverse(arr):
    arr.reverse() 
    return arr 

# 4. Uisng the reversed() function
# this returns the reverse iterator, hence use a .join() or list() method 
# because the elements are returned one by one 
def reverseUsingReversed(arr):
    arr = list(reversed(arr))
    return arr 


print(reverseUsingSwap([1,2,3,4,5]))
print(reverseUsingSlice([1,2,3,4,5]))
print(reverseUsingReverse([1,2,3,4,5]))
print(reverseUsingReversed([1,2,3,4,5]))
    