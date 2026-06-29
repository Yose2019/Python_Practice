# the program requires to extrcat unique values from the values of the dictioanry 


data = {'gfg' : [5,6,7,8],' is' : [10,11,7,5], 'best' : [6,12,10,8], 'for' : [1,2,5]}

# for uniqueness use set 

s = set()
s = {i for value in data.values() for i in value}
print(s)