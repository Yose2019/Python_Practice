# the given program requires to split the array at the kth position
# essentially it is the same as rotation 
# the splicing method remains the same 


# here is the alegory for the current method being used 
# the current method to be implemented will use the modulo operator

# consider we have the list as follows [1, 2, 3, 4, 5, 6, 7, 8]
# now if the list is repeated and appended it would appear like this -
# [1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8]
# when a position is given , we essentially shift from the current position by the given
# number of times

# so rather wasting space by appending and stretching
# use a modulo as it is rotation and repetation

def splitArrayAndAdd(arr, shift:int):
    arr = [arr[(i + shift) % len(arr)] for i in range(len(arr))]
    return arr 

print(splitArrayAndAdd([1,2,3,4,5,6,7,8,9], -5))