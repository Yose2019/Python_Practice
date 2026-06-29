# the program counts all the characters which are of length n 

text = r'D:\practice\File handling programs\nchar.txt'
n = int(input('Enter the length needed:'))
count = 0
lst = []
with open(text, 'r') as f:
    word = ''
    for ch in f.read():
        if ch.isalnum():
            word += ch

        if ch == " " or ch == '\t' or ch == '\n':
            if len(word) == n:
                count += 1 
                lst.append(word)
            word = ''

    # checking the last word    
    if len(word) == n:
        count += 1
        lst.append(word)
print(count)
print(lst)

        
