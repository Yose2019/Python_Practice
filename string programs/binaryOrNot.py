# the given program checks whether the string is binary or not 
# a binary string is a string which only consists of 0's and 1's 

# different methods are discussed in the same program 

# the looping method 
def LoopAndCheck(s : str) -> bool :
    for chr in s:
        if chr not in '01':
            return False 
        
    return True 

# using all method 
def usingAll(s : str) -> bool : 
    if all(c in "01" for c in s):
        return True 
    return False 

print(LoopAndCheck("00001111010101010"))
print(LoopAndCheck("0000111243010101010"))
print(usingAll("00001111010101010"))
print(usingAll("000011232410101010"))
print()

# other methods include using set and checkin whether it was a subset or not 