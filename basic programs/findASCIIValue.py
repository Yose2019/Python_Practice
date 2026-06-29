# here we will use the inbuilt function called ord()

import random

def ASCII(char:str):
    return ord(char)

char_set = [chr(random.randint(ord('a'),i)) for i in range(ord('a'), ord('z'))]

for i in char_set:
    print(ASCII(i))

# alternatively can also use string formatting
# print("Ascii of %s is %d"%('c','c'))
# can also use int(character) to get it's ASCII value