# The program checks whether a given word is present in the text file or not
# if not then it says so and if yes then it give the line number
# if it occurs multiple times then the first occurence is returned 

# different methods are discussed in the same program 

word1 = input("Enter the word to be found:")

# 1. Using the manual counter 
with open(r"D:\practice\File handling programs\nchar.txt", 'r') as f:
    count = 0; flag = False;
    for lines in f.readlines():
        count += 1 
        if word1 in lines.split():
            flag = True
            print(count)
            break 
    if not flag:
        print("Word doesn't exist in the file")


# 2. Using an enumerate function 
word2 = input("Enter the other word needed to be found:")

with open(r"D:\practice\File handling programs\nchar.txt", 'r') as f:
    flag = False 
    for num, line in enumerate(f, start = 1):
        if word2 in line.strip():
            print(num)
            flag = True
            break # if break is not given all occurences can be tracked 
        
    if not flag :
        print("Word doesn't exist in this file")