"""
In English, ordinal numerals have suffixes such as the ―th‖ in ―30th‖ or ―nd‖ in ―2nd‖. Write an 
ordinalSuffix() function with an integer parameter named number and returns a string of the 
number with its ordinal suffix. For example, ordinalSuffix(42) should return the string 
'42nd'. 
You may use Python’s str() function to convert the integer argument to a string. Python’s 
endswith() string method could be useful for this exercise, but to maintain the challenge in this 
exercise, don’t use it as part of your solution. 
These Python assert statements stop the program if their condition is False. Copy them to 
the bottom of your solution program. Your solution is correct if the following assert statements’ 
conditions are all True: 
assert ordinalSuffix(0) == '0th' 
assert ordinalSuffix(1) == '1st' 
assert ordinalSuffix(2) == '2nd' 
assert ordinalSuffix(3) == '3rd' 
assert ordinalSuffix(4) == '4th' 
assert ordinalSuffix(10) == '10th' 
assert ordinalSuffix(11) == '11th' 
assert ordinalSuffix(12) == '12th' 
assert ordinalSuffix(13) == '13th' 
assert ordinalSuffix(14) == '14th' 
assert ordinalSuffix(101) == '101st' 
Try to write a solution based on the information in this description. If you still have trouble 
solving this exercise
"""

def ordinalSuffix(number : int):
    num_string = str(number)
    num = num_string[-2:]
    
    if num in ['11', '12', '13']:
        return num + 'th'
    else:
        if num[-1] == '1':
            return num_string + 'st'
        elif num[-1] == '2':
            return num_string + 'nd'
        elif num[-1] == '3' :
            return num_string + 'rd'
        else:
            return num_string + 'th'
    
assert ordinalSuffix(0) == '0th' 
assert ordinalSuffix(1) == '1st' 
assert ordinalSuffix(2) == '2nd' 
assert ordinalSuffix(3) == '3rd' 
assert ordinalSuffix(4) == '4th' 
assert ordinalSuffix(10) == '10th' 
assert ordinalSuffix(11) == '11th' 
assert ordinalSuffix(12) == '12th' 
assert ordinalSuffix(13) == '13th' 
assert ordinalSuffix(14) == '14th' 
assert ordinalSuffix(101) == '101st' 


# takeaway- reverse indexes or negative indexes are crucial 