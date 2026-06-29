# the program requires to copy the odd nnumbered lines of one file to another 
# the other file is a new file 

f1 = r"D:\practice\File handling programs\ex2.txt"
f2 = r"D:\practice\File handling programs\ex_new.txt"

f = open(f2, 'w')
f.close()

with open(f1, 'r') as file1, open(f2, 'a') as file2:
    for num, line in enumerate(file1, start=1):
        if num % 2 != 0:
            file2.write(line)

'''
with open('input.txt', 'r') as infile:
    lines = infile.readlines()

with open('output.txt', 'w') as outfile:
    for line in lines[0::2]: 
        outfile.write(line)

this is an alternate way of doing the same program 
'''