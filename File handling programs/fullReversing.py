 # the program of full reversing completely reverses the file 

# 1. Reverse the lines 
# 2. Reverse the word order 
# 3. Reverse the letters in the words 

# lines = []
# words = []

# with open(r"D:\practice\File handling programs\example.txt", 'r') as f:
#     # add lines and reverse the lines
#     for line in f:
#         lines.append(line.strip())
#     lines = lines[::-1]

#     # then reverse the words in eah index and along with then 
#     # reverse the letters in the word 
#     for index, line in enumerate(lines):
#         lines[index] = " ".join(line.split()[::-1])  
#         lines[index] = lines[index][::-1] 
#         lines[index] += '\n'



# with open(r"D:\practice\File handling programs\example.txt", 'w') as f:
#     for line in lines:
#         f.write(line)


# another way of handling this is 
# using read lines 
text = ""
with open(r"D:\practice\File handling programs\example.txt", 'r') as f:
    text = f.read()

print(text)

with open(r"D:\practice\File handling programs\example.txt", 'w') as f:
    f.write(text[::-1])

