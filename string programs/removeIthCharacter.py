# remove the ith character from the string 
# different methods are discussed in the same program 
# a key point to note is that string are immutable 

# using slicing of the string
def usingSlicing(s, i):
    return s[:i] + s[i+1:] 

# converting string to list and remove by list methods 
def usingList(s, i):
    s = list(s)
    del s[i]
    return "".join(s)

# using the list and for loop 
def usingListandLoop(s, i):
    s = list(s)
    s_new = ""
    for ind in range(len(s)):
        if ind == i:
            continue 
        else:
            s_new += s[i]

    # note - same an be done without converting to list as well wiht new string and iteration 

    return "".join(s)

print(usingSlicing("appleMartin", 8))
print(usingList("appleMartin", 8))
print(usingListandLoop("appleMartin", 8))

