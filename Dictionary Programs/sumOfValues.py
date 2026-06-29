# find the sum of all dictionary values

data = {'a': 100, 'b': 200, 'c': 300}

# first checking whether all the values are integers or not

verdict = all( (i==int(i) or i == float(i)) for i in data.values())

if verdict:
    print(sum(data.values()))
else:
    raise ValueError("Data values must be interger or float not string")


              