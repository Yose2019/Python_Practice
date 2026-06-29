#to find the maximum of two numbers 
#also use functions to decribe it

def findMaximum(a:int,b:int):
    if a>b:
        return a
    elif a<b:
        return b
    else:
        return "Both are equal"
    
print(findMaximum(1,1))