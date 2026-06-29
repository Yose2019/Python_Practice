# given a string of words, reverse the order of the words in the given string 
# note not to reverse the letters in the words 
# that is - 'what a great day' as 'day great a what' 

# different methods are discussed here in the program  

# 1. Using split and join 
def reverseWordOrderBySplitAndJoin(s : str) -> str: 
    s = " ".join(s.split()[::-1])
    return s 

# 2. Using split and loops 
def reverseWordOrderByLoops(s : str) -> str:
    words = s.split()
    s = ""

    for i in range(len(words)):
        s += words[-i-1] + " "

    s = s.strip()
    return s 


print(reverseWordOrderBySplitAndJoin('day great a what'))
print(reverseWordOrderByLoops('Behen aise hi chala kar, proud of you'))