# check whether the given strings are symmetrical and palindrome
# any method from the previosuly discussed palindrome program can be used to check palindrome
# now for symmetry - it is considered the case as such - ababa ( ab != ba)
# symmetrical indicates the first half and second half of the string should be identical

def symmetryAndPalindrome(s : str):
    pal = True if s == s[::-1] else False 

    print("String is palindrome" if pal == True else "not palindrome")
    
    half = len(s)//2 

    sym = s[:half] == s[half:] if len(s) % 2 == 0 else s[:half] == s[half+1:]

    print("String is symmetric" if sym == True else "not symmetric")
    print()

    return 


print(symmetryAndPalindrome('Falafel'))
print(symmetryAndPalindrome('ammamma'))
print(symmetryAndPalindrome('ambam'))
print(symmetryAndPalindrome('konkan'))

