# this program discusses how to find the second largest element in a list 
# different approaches are discussed in the same program 

# 1. This program uses the traversing method and logical comparison
# in order to find the second largest element 
def secondLargestElement(arr):
    hst = hst2 = float('-inf')

    for i in arr:
        if i > hst:
            hst2 = hst
            hst = i 
        elif i > hst2 and i < hst:
            hst2 = i 

    return hst2 if hst2 != float('-inf') else None 

# 2. This method uses sort, we can either sort in reversed order 
# and return the second element - arr[1]
# or sort in regular order and return the second element from the right - arr[-2]
def secondLargestBySort(arr):
    arr.sort(reverse = True)
    return arr[1]

print(secondLargestElement([2, 3, 5, 7, 1, 0, -1]))
print(secondLargestBySort([-11, -10, -34, -21, -1, 0 , 5, 6, -9]))
print(secondLargestElement([2,2,2,2,2,2]))