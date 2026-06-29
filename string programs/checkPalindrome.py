# the crucial thing which sets strings apart from list is that they are immutable 
# so we are gonna discuss this here 

# this program checks whether the string is palindrome or not
# a palindrome essentially reads the same forward and backward - like mom, malayalam 

#  different methods are discussed in the same program 

# 1. Palindrome using loops 
def palindromeByLoops(s : str) -> bool:
    n = len(s)
    for i in range(n//2):
        if s[i] != s[n-i-1]:
            return False
        
    return True

# 2. checking whether the reversed string is same 
def palindromeByReverse(s : str) -> bool:
    if s == s[::-1] :
        return True 
    
    return False 

# 3. Similar to loops we have recursion 
def palindromeUsingRecursion(s : str, i : int, n : int) -> bool:
    if i == n//2 :
        return True 
    
    if s[i] == s[n - i - 1] :
        return palindromeUsingRecursion(s, i+1, n)
    else :
        return False 
    

# 4. Using the all function 
def palindromeUsingAll(s : str) -> bool:
    if all([s[i] == s[-i-1] for i in range(len(s)//2)]) : 
        return True
    return False 

'''
Another method is using the inbuilt reversing function  
rev = ''.join(reversed(s))
'''

print(palindromeByReverse('malayalam'))
print(palindromeByLoops('kumar'))
print(palindromeUsingRecursion('ammba', 0, len('ammba')))
print(palindromeUsingAll('malayalam'))

        




    


