# This program discusses how to obtain the product of elements from the list
# all the approaches are discussed in the same program 

from math import prod

# 1. Using the inbuilt function 'prod' from the math module 
def productUsingProd(arr):
    return prod(arr) 


# 2. By traversing the list 
def productByTraversing(arr):
    product = 1
    for i in arr:
        product *= i 

    return product


print(productUsingProd([1,2,3,4]))
print(productByTraversing([1,5,7,2]))
