# the given program requires to rotate the string the number of times given in the string

s = "GeeksforGeeks"
d = 2

# the above mentions the number of rotations 
# not indexes 

# before getting into program 
# left rotation twice - ksGeeksforGee 
# right rotattion twice - eksforGeeksGe 
# essentially, split the last d characters from the end and append them 
# and append it to front for left rotation
# vice versa for the right rotation 

# let us consider positive integer for right rotation and negative integer for left rotation 

left_rotated = s[-d:] + s[:-d]
right_rotated = s[d:] + s[:d]

print("Left rotated string : ", left_rotated)
print("Right rotated string : ", right_rotated)


# doing it manually 
def manualRotation(s:str, d:int) -> str:
    left_rotated = ""
    for i in range(len(s) - d, len(s)):
        left_rotated += s[i]
    for i in range(len(s) - d):
        left_rotated += s[i]

    right_rotated = ""
    for i in range(d, len(s)):
        right_rotated += s[i]
    for i in range(d):
        right_rotated += s[i]

    return left_rotated, right_rotated

lrs, rrs = manualRotation(s, d)
print("Left rotated : ", lrs,": Right rotated : ", rrs)
