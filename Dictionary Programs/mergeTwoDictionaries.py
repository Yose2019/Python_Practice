# the program gives the method to merge two dictionaries 

d1 = {'a':1, 'b':2}
d2 = {'b':2, 'd':4}

# we cannot use the + operator directly to concatenate 


# set default is one method
for key in d2.keys():
    d1.setdefault(key, d2[key])

d3 = {'a':1, 'b':2}

# another method is as follows 
for key in d2.keys():
    d3[key] = d2[key]


print("d1 : ", d1)
print("d3 : ", d3)

# the other methods are as follows 

# using the update method 
d4 = {'a':1, 'b':2}
d4.update(d2)
print("d4 with update is : ", d4)

# using the | operator 
d5 = {'a':1, 'b':2}
print("d5 using | operator : ", d5 | d2)

# using unpacking 
d6 = {**d1, **d2}
print("d6 with unpacking is : ", d6)

