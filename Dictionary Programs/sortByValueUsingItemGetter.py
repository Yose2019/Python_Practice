# the program uses itemgetter from operater module to sort the list of dictonary based on the values
# ideally if we use the sorted we just sort it using keys 

# courtesy of knowledge - geeksForGeeks 

from operator import itemgetter

d = [{'name':"Shristhi", "age":19}, {"name":"Apple", "age":10}]

print(sorted(d, key=itemgetter("age")))