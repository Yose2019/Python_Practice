'''
Write a isLeapYear() function with an integer year parameter. If year is a leap year, the 
function returns True. Otherwise, the function returns False. 
These Python assert statements stop the program if their condition is False. Copy them to 
the bottom of your solution program. Your solution is correct if the following assert statements’ 
conditions are all True: 
assert isLeapYear(1999) == False 
assert isLeapYear(2000) == True 
assert isLeapYear(2001) == False 
assert isLeapYear(2004) == True 
assert isLeapYear(2100) == False 
assert isLeapYear(2400) == True 
Try to write a solution based on the information in this description. If you still have trouble 
solving this exercise, read the Solution Design and Special Cases and Gotchas sections for 
additional hints. 
Prerequisite concepts: modulo operator, elif statements 
'''

'''
Leap year are divisible by 4, can also be divisible by 400, but not by 100
'''

def isLeapYear(year : int):
    if not year % 4:
        if not year % 400:
            return True
        if not year % 100:
            return False
        return True
    
    return False 

assert isLeapYear(1999) == False 
assert isLeapYear(2000) == True 
assert isLeapYear(2001) == False 
assert isLeapYear(2004) == True 
assert isLeapYear(2100) == False 
assert isLeapYear(2400) == True
