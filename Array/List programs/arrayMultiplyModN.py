# the given program requires array multiplication and find reminder when mod by n(num of elements)
# all the numbers are multiplied together and then reminder is obtained

# using the naive approach

def arrayMultiply(arr):
    mul:int = 1

    n:int = len(arr)

    for i in arr:
        mul *= i

    return mul % n 

print(arrayMultiply([2,2,2,2,2]))

