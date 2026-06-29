# The program prints all positive numbers in a range of numbers given a starting and end point 
# Different methods are discussed in the same program 

# 1. This method uses the looping method with for loop
def usingForLoop(start, end):
    arr = []
    for i in range(start, end + 1):
        if i >= 0:
            arr.append(i)

    return arr 

# 2. This method uses the looping method with while loop
def usingWhileLoop(start, end):
    arr = []
    while start <= end:
        if start >= 0:
            arr.append(start)
        start += 1

    return arr 

# 3. This method uses list comprehension
def usingListComprehension(start, end):
    arr = [i for i in range(start, end + 1) if i >= 0]
    return arr 


# 4. Using Lambda functions 
def usingLambda(start, end):
    arr = list(filter(lambda x : x>=0, range(start, end + 1)))
    return arr 

print(usingForLoop(-2,6))
print(usingWhileLoop(-3,0))
print(usingListComprehension(-5,-1))
print(usingLambda(3,6))


'''
THE PROGRAM WILL REMAIN THE SAME FOR NEGATIVE NUMBERS IN THE RANGE WITH THE EXCEPTION OF 
CONDITION , WHICH WILL CHECK FOR NUMBER < 0


ADDITIONALLY THE PROGRAM CAN HAVE CONDITION TO CHECK WHETHER THE START < END TO
AVOID EMPTY LIST 
'''