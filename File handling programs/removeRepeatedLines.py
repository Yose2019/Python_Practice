# the program removes repeated lines from the text file 
# let us create a text file which has repeated lines 

def createAndWriteFile():
    f_write = open('sampleFile.txt', 'w')

    while True:
        inp = input('Enter content or nadie entroda to stop:')
        if inp.lower() == 'nadia entroda':
            break
        f_write.write(inp+'\n')
         

    f_write.close()

    return 

# now we have two ways in which this program can be executed 
# method 1 is : using the set which naturaly prevents duplicated from occuring 

createAndWriteFile()
s = set()
with open('sampleFile.txt', 'r') as f:
    for line in f:
        s.add(line)

print(s)

with open('sampleFile.txt', 'w') as f:
    for line in s:
        f.write(line)


# now the same program with lists 
# createAndWriteFile()
# l = []
# with open('sampleFile.txt', 'r') as f:
#     for line in f:
#         if line not in l:
#             l.append(line)

# print(l)

# with open('sampleFile.txt', 'w') as f:
#     for line in l:
#         f.write(line)


'''
a new file can be created as well and written into it
'''




