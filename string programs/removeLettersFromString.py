# the given program shows methods in which the given letter in a particular string
# can be removed from the word
# note that string is immutable

# different methods are discussed in the same program 

# 1. Using replace
def removeLettersUsingReplace(s : str, letter : str) :
    s = s.replace(letter, '')
    return s 

# 2. Using list, in and loops 
def removeLettersUsingLoops(s : str, letter : str) :
    s = list(s) # split won't split the word into letters
    while letter in s :
        s.remove(letter)

    s = "".join(s)

    ''' The above program in list comprehension can be written as 
    s = "".join([i for i in s if i != letter])
    '''
    return s

print(removeLettersUsingReplace("banana", 'a'))
print(removeLettersUsingLoops("banana", 'a'))
     
