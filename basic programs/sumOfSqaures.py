# sum of squares of first n natiral numbers

n = int(input("Enter n:"))

print(sum([i**2 for i in range(1,n+1)]))

# using for loop 

summation = 0

for i in range(1, n+1):
    summation = summation + (i**2)

print(summation)