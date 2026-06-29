'''
Write a mode() function that has a numbers parameter. This function returns the mode, or 
most frequently appearing number, of the list of integer and floating-point numbers passed to the 
function. 
These Python assert statements stop the program if their condition is False. Copy them to 
the bottom of your solution program. Your solution is correct if the following assert statements’ 
conditions are all True: 
assert mode([]) == None 
assert mode([1, 2, 3, 4, 4]) == 4 
assert mode([1, 1, 2, 3, 4]) == 1 
import random 
random.seed(42) 
testData = [1, 2, 3, 4, 4] 
for i in range(1000): 
random.shuffle(testData) 
assert mode(testData) == 4 
Shuffling the order of the numbers should not affect the mode. The for loop does 1,000 such 
random shuffles to thoroughly check that this fact remains true. For an explanation of the 
random.seed() function, see the Further Reading section of Exercise #19, ―Password 
Generator‖. 
Try to write a solution based on the information in this description. If you still have trouble 
solving this exercise, read the Solution Design and Special Cases and Gotchas sections for 
additional hints. 
'''

def mode(lst):
    if not len(lst):
        return None 
    
    count_num = {}
    max_count = 0
    mode_num = 0
    for i in lst:
        count_num[i] = count_num.get(i, 0) + 1
        if count_num[i] > max_count:
            max_count = count_num[i]
            mode_num = i

    return mode_num

assert mode([]) == None 
assert mode([1, 2, 3, 4, 4]) == 4 
assert mode([1, 1, 2, 3, 4]) == 1 
import random 
random.seed(42) 
testData = [1, 2, 3, 4, 4] 
for i in range(1000): 
    random.shuffle(testData) 
    assert mode(testData) == 4 