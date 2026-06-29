'''
Write a generatePassword() function that has a length parameter. The length 
parameter is an integer of how many characters the generated password should have. For security 
reasons, if length is less than 12, the function forcibly sets it to 12 characters anyway. The password 
string returned by the function must have at least one lowercase letter, one uppercase letter, one 
number, and one special character. The special characters for this exercise are ~!@#$%^&*()_+.  
Your solution should import Python’s random module to help randomly generate these 
passwords. 
These Python assert statements stop the program if their condition is False. Copy them to 
the bottom of your solution program. Your solution is correct if the following assert statements’ 
conditions are all True: 
assert len(generatePassword(8)) == 12 
pw = generatePassword(14) 
assert len(pw) == 14 
hasLowercase = False 
hasUppercase = False 
hasNumber = False 
hasSpecial = False 
for character in pw: 
if character in LOWER_LETTERS: 
hasLowercase = True 
if character in UPPER_LETTERS: 
58 
Python Programming Exercises, Gently Explained 
hasUppercase = True 
if character in NUMBERS: 
hasNumber = True 
if character in SPECIAL: 
hasSpecial = True 
assert hasLowercase and hasUppercase and hasNumber and hasSpecial 
Try to write a solution based on the information in this description. If you still have trouble 
solving this exercise, read the Solution Design and Special Cases and Gotchas sections for 
additional hints. 
Prerequisite concepts: import statements, random module, strings, string concatenation, 
len(), append(), randint(), shuffle(), join() 
'''
import random 

def generatePassword(length) : 
    if length < 12:
        length = 12 

    password = []

    ll = [chr(i) for i in (range(ord('a'), ord('z') + 1))] 
    ul = [chr(j) for j in (range(ord('A'), ord('Z') + 1))] 
    num = [i for i in range(0, 10)] 
    spe = list('~!@#$%^&*()_+')

    password.append(str(random.choice(ll)))
    password.append(str(random.choice(ul)))
    password.append(str(random.choice(num)))
    password.append(str(random.choice(spe)))

    lst = ll + ul + num + spe

    for i in range(length - 4):
        password.append(str(random.choice(lst)))
        random.shuffle(lst)


    return "".join(password)

LOWER_LETTERS = [chr(i) for i in range(ord('a'), ord('z') + 1)]
UPPER_LETTERS = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
NUMBERS = [str(i) for i in range(0, 10)]
SPECIAL = list('~!@#$%^&*()_+')

assert len(generatePassword(8)) == 12 
pw = generatePassword(14) 
print(pw)
assert len(pw) == 14 
hasLowercase = False 
hasUppercase = False 
hasNumber = False 
hasSpecial = False 
for character in pw: 
    if character in LOWER_LETTERS: 
        hasLowercase = True 
    if character in UPPER_LETTERS: 
        hasUppercase = True    
    if character in NUMBERS: 
        hasNumber = True 
    if character in SPECIAL: 
        hasSpecial = True 
assert hasLowercase and hasUppercase and hasNumber and hasSpecial    