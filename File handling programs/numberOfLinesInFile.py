# The program counts the number of lines in a text file 
# the program although we can say assumes there aren't spaces in between them or 
# empty lines or paragraph spaces and may consider them as line as well
# for that a conditional check is included 
# different methods are discussed in the same program 


# 1. using a manual counter 
with open(r"D:\practice\File handling programs\nchar.txt", 'r') as f:
    count = 0
    for line in f:
        if len(line.strip()) != 0:
            count += 1
    print(count) 

# 2. using sum() function and loop 
with open(r"D:\practice\File handling programs\nchar.txt", 'r') as f:
    lines = sum(1 for line in f if len(line.strip()) != 0)
    print(lines) 

# 3. Using readlines() method 
with open(r"D:\practice\File handling programs\nchar.txt", 'r') as f:
    lines = len(f.readlines()) # this may not consider the conditional exception
    print(lines)