# the program removes lines from the text file which start with a given prefix 
# the core idea that one should remember is that when you pass
# through the pointer in the program 
# then each line is considered as a string 
# and strings have inbuilt function starts with 

prefix = "This"

file = r"D:\practice\File handling programs\ex3.txt"
toEdit = []

with open(file, 'r') as f:
    for line in f:
        if not line.startswith(prefix):
            toEdit.append(line.strip())

with open(file, 'w') as f:
    for line in toEdit:
        if line!='':
            f.write(line + '\n')
        

print(toEdit)


# The only issue the above program might have is the additional space consumption
# by the list in case of larger files
# an alternate is open a new file in write mode 

'''
f_edit = the old file path opened in read mode
f_new = the new file path opened in write mode ( if doesn't exists then write mode creates one)

for line in f_edit:
if not line.startswith(prefix):
f_new.write(line)
'''


'''
another alternate is using the find() method
find method returns the index of the first character of prefix in the string 
so check whether it is not equal to 0 as 0 indicates it was in the starting position
of the string and thus the line
'''
