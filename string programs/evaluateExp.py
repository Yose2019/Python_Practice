# the given program discusses how can the expression be evaluated if it is a part of a string

exp = "x = 5\ny = 10\nprint(x + y)"

# method 1 
# splitting the string at the \n 
list_of_elements = exp.split("\n")
print(list_of_elements)

for line in list_of_elements:
    exec(line)

# expression which returns a value automatically printed 
# we can also do 

exec(exp)