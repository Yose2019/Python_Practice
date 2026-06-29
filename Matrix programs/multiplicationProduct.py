# the program given is used to find the product of all elements in the 2-d list 

'''
The simplest methods are to find the products in the list using the prod function 
over a unidimentional list in numpy and math 
'''

import numpy as np
import math as m 

a = [[1, 4, 5], [7, 3], [4], [46, 7, 3]]

uniDL = [ele  for row in a for ele in row]

productNumpy = np.prod(uniDL)
productMath = m.prod(uniDL)

print(productNumpy)
print(productMath)

'''
Brute force approach 
'''
prod = 1
for row in a:
    for ele in row :
        prod *= ele
print(prod)