# this is the program to check whether an array is monotonic or not
# now checking this we need to ensure that whether it is strictly increasing
# or the array is strictly decreasing

'''
-- here we use the all() functions 
-- now all checks the iterables whether true or not
-- all([True, True]) GIVES TRUE
'''

def monotonicArray(arr) -> bool:
    if len(arr) <= 2:
        return True 
    
    inc:bool= all([arr[i] <= arr[i+1] for i in range(0, len(arr) - 1)])
    dec:bool= all([arr[i] >= arr[i+1] for i in range(0, len(arr) - 1)])

    return inc or dec 

print(monotonicArray([1,2,3,4,5,6]))
print(monotonicArray([-1,-2,-3,-4,-5,-6]))
print(monotonicArray([1,2,3,4,6,5]))
print(monotonicArray([1,2])) 
