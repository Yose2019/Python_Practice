# The given program is for file handling in python
# This program is used to read the file and print each word in the file 

with open(r'D:\practice\File handling programs\example.txt', 'r') as f:
    for line in f:
        for word in line.split():
            print(word)
        
# the key thing to notice here is that split fucntion, in case not specified 
# splits at the tabs or spaces 
# and the next line is handled
# with open allows the privilege of closing the file without mentioning specially
# another emthod using .read() method is discussed below
print()
print("THIS IS THE OTHER PROGRAM")
print()

with open(r'D:\practice\File handling programs\example.txt', 'r') as f:
    word = ""
    for ch in f.read():
        if ch == " " or ch == "\n":
            print(word)
            word = ''
        else:
            word += ch 
            