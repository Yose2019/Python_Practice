# find the largest element / maximum in an array

import math

def findMaximum(array):
    if len(array) == 0:
        return 0
    
    maximum = array[0]

    for i in array:
        if i > maximum:
            maximum = i

    return maximum

print(findMaximum([-9,-10]))
