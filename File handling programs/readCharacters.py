# the program reads each individual character from the string or word
# printing whitespaces is not an issue as it is also considered a character here 

# different methods are discussed in the same program 

# 1. Using two loops 
with open(r'D:\practice\File handling programs\example.txt', 'r') as f:
    for line in f:
        for ch in line:
            if ch == '\n':
                print('New line here')
                continue
            print(ch)


# 2. Using the .read(size) method until the pointer f stops encountering a chracter 
with open(r'D:\practice\File handling programs\example.txt', 'r') as f:
    while True:
        ch = f.read(1)
        if ch:
            print(ch)
        else:
            break 

# 3. Else another method is simply loop over using .read() method 
with open(r'D:\practice\File handling programs\example.txt', 'r') as f:
    for ch in f.read():
        print(ch)