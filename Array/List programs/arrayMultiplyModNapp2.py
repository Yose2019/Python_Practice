# the naive approach discussed in program "arrayMultiplyModN"
# does not take into consideration that large numbers of product cannot be handled
# so we use this technique instead - (a*b) % n = ((a % n) * (b % n)) % n 

# algorithm would suggest
# go through each variable , perform mod twice , multiply it with the variable storing product

def arrayMultiplyModN(arr):
    mul:int = 1
    n:int = len(arr)

    for i in arr:
        mul = (mul * (i % n)) # this is also okay - (mul * (i % n)) % n - have to ret only mul

    return mul % n

print(arrayMultiplyModN([2,2,2,2,2])) 
