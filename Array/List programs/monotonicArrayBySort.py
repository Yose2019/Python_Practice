# check monotonicity of array by sorted function

def monotonicArray(arr) -> bool :
    if len(arr) <= 2:
        return True 
    
    inc = (arr) == sorted(arr)
    dec = (arr) == sorted(arr, reverse= True) 

    return inc or dec 

print(monotonicArray([1,2,3,4,5,6]))
print(monotonicArray([-1,-2,-3,-4,-5,-6]))
print(monotonicArray([1,2,3,4,6,5]))
print(monotonicArray([1,2]))