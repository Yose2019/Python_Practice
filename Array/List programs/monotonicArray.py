# the given array is said to be monitonic if it is either strictly increasing
# or if the array is strictly decreasing 
# either has to be true 

# approach one is the looping approach which we go through
'''
-- in this approach we compute the following 
-- we first compute the difference between initial two elements
-- it can be either positive or negative ( either tells the direction )
-- but it has to remain true throughout 
-- always make sure to check for increasing and decreasing separately
'''

def monotonicArray(arr) -> bool:
    inc = dec = True 

    if len(arr) < 2:
        return True
    
    for i in range(1, len(arr)):
        # for increasing order
        if (arr[i] <= arr[i-1]):
            inc = False 
        if (arr[i] >= arr[i-1]):
            dec = False
    
    return inc or dec 

print(monotonicArray([1,2,3,4,5,6]))
print(monotonicArray([-1,-2,-3,-4,-5,-6]))
print(monotonicArray([1,2,3,4,6,5]))