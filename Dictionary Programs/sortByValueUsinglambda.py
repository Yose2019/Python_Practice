# the program uses lambda functions to sort the list of dictonary based on the values
# ideally if we use the sorted we just sort it using keys 

# courtesy of knowledge - geeksForGeeks 

d = [{'name':"Shristhi", "age":19}, {"name":"Apple", "age":10}]

print(sorted(d, key=lambda x : x['age']))