# the python program requires to identify words which are not common in two strings 

# different methods are discussed in the same program 

# 1. the method uses sets 
def usingSet(s1 : str, s2 : str) : 
    s1 = set(s1.split(" "))
    s2 = set(s2.split(" "))

    return list(s1 ^ s2)

print(usingSet("apple is good", "apple is mango")) 

# using loops 
def usingLoops(s1 : str, s2 : str):
    s1 = s1.split(" ")
    s2 = s2.split(" ") 

    lst = []

    lst += [word for word in s1 if word not in s2]
    lst += [word for word in s2 if word not in s1]

    return lst 

print(usingLoops("apple is good", "apple is mango")) 


# the other method is finding which words appear only once after combining the strings or lists