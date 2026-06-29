# sum of cubes of first n natiral numbers

n = int(input("Enter n:"))

print(sum([i**3 for i in range(1,n+1)]))

# using for loop 

summation = 0

for i in range(1, n+1):
    summation = summation + (i**3)

print(summation)