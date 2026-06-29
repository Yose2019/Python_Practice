# the program discusses method to convert the list of key-value pait tuples into dictionary
# into a flat dictionary 

list_of_key_value_pair = [("name", "Ak"), ("age", 25), ("city", "NYC")] 

d = {}

# a few methods are discussed here 
for pair in list_of_key_value_pair:
    d[pair[0]] = pair[1]

print(d)


# we can directly use dict() for this 
d1 = {}
d1 = dict(list_of_key_value_pair) 

print(d1)

# using comprehension 
d2 = {key : value for key, value in list_of_key_value_pair}
print(d2)

# using for loop in a different way 
d3 = {}
for key, value in list_of_key_value_pair:
    d3[key] = value