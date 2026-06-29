# find all the even elements in the range of given numbers 
# different approaches are discussed in the same program 

# primarily these use the range() function 

# 1. Just skip over the elements by mentioning the steps in the range function 
def usingRangeStep(start, end):
    lst = []
    start += (start + 1) % 2 
    for i in range(start, end + 1, 2):
        lst.append(i)

    return lst 

# 2. Check using loops 
def usingLoop(start, end):
    lst = []
    for i in range(start, end + 1):
        if i % 2 == 0:
            lst.append(i)

    return lst 

# 3. Check using list comprehension 
def usingListComprehension(start, end):
    lst = [i for i in range(start, end + 1) if i % 2 == 0]
    return lst 

print(usingRangeStep(2,10))
print(usingRangeStep(5,15))
print(usingLoop(2, 20))
print(usingListComprehension(1,13))

# ODD ELEMENTS IN A RANGE ALSO CAN BE DONE USING THE SAME PROGRAM WITH THE EXCEPTION OF CONDITION
# CAN USE THE CONDITION FOR CHECKING ODD NUMBER 
# ALSO THE START , IF IT IS ODD IT MODIFIES IT TO EVEN 
