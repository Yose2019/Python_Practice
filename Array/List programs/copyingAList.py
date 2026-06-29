# The program copies from list to another list
# the take-away from this program is that list should not be directly assigned to
# new variable , as a = [], and b = a , does not create a list
# rather this assigns the vaiable to the same memory location 
# this causes changes to appear in the main list irrespective of 
# it being perfomed on the copied list 
# Different methods to copy a list at a new memory location is discussed in the program
# The virtual memory address ( not the RAM address physical) can be
# printed and compared

from copy import deepcopy

# 1. Using the .copy() method
def usingCopyMethod(arr):
    lst = arr.copy()
    print('Main array:',hex(id(arr)),'Copied array:',hex(id(lst)))
    return lst

# 2. Using the deepcopy from copy module 
def usingDeepcopy(arr):
    lst = deepcopy(arr)
    print('Main array:',hex(id(arr)),'Copied array:',hex(id(lst)))
    return lst 

# 3. Uisng list comprehension
def usingListComprehension(arr):
    lst = [x for x in arr]
    print('Main array:',hex(id(arr)),'Copied array:',hex(id(lst)))
    return lst 

# 4. Using assignment along with the list() function 
def usingListAndAssignment(arr):
    lst = list(arr)
    print('Main array:',hex(id(arr)),'Copied array:',hex(id(lst)))
    return lst 

# 5. Using assignment along with slicing 
def usingSlicingAndAssignment(arr):
    lst = arr[:]
    print('Main array:',hex(id(arr)),'Copied array:',hex(id(lst)))
    return lst 

print(usingCopyMethod([1,2,3]))
print(usingDeepcopy([1,2,3]))
print(usingListAndAssignment([1,2,3]))
print(usingListComprehension([1,2,3]))
print(usingSlicingAndAssignment([1,2,3]))