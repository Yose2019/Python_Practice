# swap the first and last elements of the array
# both methods, a simple swap and the unpacking one are discussed in the same program

def swapFirstAndLastElement(arr):
    if len(arr) < 2:
        return arr
    
    arr[0], arr[-1] = arr[-1], arr[0]

    return arr 

def swapFirstAndLastByUnpacking(arr):
    if len(arr) < 2:
        return arr
    
    a, *unpack, b = arr 

    arr = b, *unpack, a 

    return arr  # this returns a tuple

print(swapFirstAndLastElement([1,2,3,4,5]))
print(swapFirstAndLastByUnpacking([1,2,3,4,5]))