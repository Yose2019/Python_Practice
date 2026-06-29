# the program discusses the methods to remove the key from the dictionary 

data = {'a': 100, 'b': 200, 'c': 300} 

# the pop(atleast 1 argument which is key) method removes the key from the dictinary
# it returns the value
# the second method gives the default if a key is not present
d = data.pop('a')
print(d)
print(data)
d = data.pop('a', "Key not found") 
print(d)
print(data)

# another mehotd is del 
del data['b']
# and to remove key at end without passing argument we use popitem()
data.popitem()
print(data)