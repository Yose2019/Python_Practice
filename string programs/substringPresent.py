# check if the substring is present in a given string 
# different methods are discussed in the same program 

# 1. Using in method 
def usingIn(s : str, ss : str) -> str:
    if ss in s:
        return True 
    return False 

# 2. Using Find method 
def usingFind(s : str, ss : str) -> str:
    if s.find(ss) :
        return True
    return False 


print(usingIn("apartment", 'apt'))
print(usingIn("apartment", 'et'))
