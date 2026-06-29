'''
Write a program that displays the lyrics to ―99 Bottles of Beer.‖ Each stanza of the song goes like 
this: 
X bottles of beer on the wall, 
X bottles of beer, 
Take one down, 
Pass it around, 
X – 1 bottles of beer on the wall, 
The X in the song starts at 99 and decreases by one for each stanza. When X is one (and X – 1 is 
zero), the last line is ―No more bottles of beer on the wall!‖ After each stanza, display a blank line to 
separate it from the next stanza. 
You’ll know you have the program correct if it matches the lyrics at 
https://inventwithpython.com/bottlesofbeerlyrics.txt. It looks like the following: 
99 bottles of beer on the wall, 
99 bottles of beer, 
Take one down, 
Pass it around, 
98 bottles of beer on the wall, 
70 
Python Programming Exercises, Gently Explained 
71 
 
98 bottles of beer on the wall, 
98 bottles of beer, 
Take one down, 
Pass it around, 
97 bottles of beer on the wall, 
…cut for brevity… 
1 bottle of beer on the wall, 
1 bottle of beer, 
Take one down, 
Pass it around, 
No more bottles of beer on the wall! 
Try to write a solution based on the information in this description. If you still have trouble 
solving this exercis

'''
for i in range(99, -1, -1):
    print(f"{i} bottles of beer on the wall,\n{i} bottles of beer,\nTake one down,\nPass it around")
    if i - 1 == 1:
        print(f"{i - 1} bottle of beer on the wall\n")
        break
    else:
        print(f"{i -1} bottles of beer on the wall\n")

print(f"1 bottle of beer on the wall,\n1 bottle of beer,\nTake one down,\nPass it around\nNo more bottles of beer on the wall\n")
