# Given a text file containing several key-value pairs in the format key = value
# find how many times a specific key-value pair occurs in the file. 
# assuming the given key-value pair follow a certain format of representation

# one possible solution is like this 
# we can create a dictionary of dictionaries where the 
# key - value pair dictionary acts as the key of main dictionary 
# the other can become count 

dct = {}

fileName = r"D:\practice\File handling programs\keyValue.txt"

with open(fileName, 'r') as f:
    for line in f:
        string = line.strip()
        dct[string] = dct.get(string, 0) + 1

print(dct)
k = input('Enter key:')
v = input('Enter value:')
pair = k + '=' + v
print(dct.get(pair, 0))


'''

an alternate method is as follows , everything remains same 
till the for loop point

after that, we can use the condition 

if line.strip() == k + '=' + v:
count += 1

'''
        


