# find the remainder when all the elements of the array are multiplied 
# remember the theory - (a * b) % d = ((a % d) * (b % d)) % d

def remainderOfArrayMultiplication(arr, n):
    mul = 1
    for i in arr:
        mul *= (i % n)

    return mul % n 

def remainderOfArrayMultiplicationAlt(arr, n):

    mul = 1
    for i in arr:
        mul *= i 

    return mul % n 


print(remainderOfArrayMultiplication([100, 10, 5, 25, 35, 14], 11)) 
print(remainderOfArrayMultiplicationAlt([100, 10, 5, 25, 35, 14], 11))
      
