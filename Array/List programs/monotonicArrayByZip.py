# check whether the array is monotonic or not using zip() function
# zip return a list of tuples where each tuple is a pair of elements 
# use all and zip together 

def monotonicArray(arr) -> bool:
    if len(arr) <= 2:
        return True 
    
    inc:bool = all([first <= next for first, next in zip(arr[:], arr[1:])])
    dec:bool = all([first >= next for first, next in zip(arr[:], arr[1:])])

    return inc or dec

print(monotonicArray([1,2,3,4,5,6]))
print(monotonicArray([-1,-2,-3,-4,-5,-6]))
print(monotonicArray([1,2,3,4,6,5]))
print(monotonicArray([1,2]))
