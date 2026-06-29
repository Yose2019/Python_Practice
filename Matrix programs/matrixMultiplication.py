# this is the classic program of matrix multiplication

A = [[12, 7, 3],
     [4, 5, 6],
     [7, 8, 9]]

B = [[5, 8, 1, 2],
     [6, 7, 3, 0],
     [4, 5, 9, 1]]

# the classic method using three loops 
prod = [[0]*len(B[0]) for _ in range(len(A))]

for r in range(len(A)):
    for c in range(len(B[0])):
        sum = 0
        for k in range(len(A[0])):
            sum += ( A[r][k] * B[k][c])

        prod[r][c] = sum 

for row in prod:
    print(row)


# another simple method is using numpy and dot method 

from numpy import dot 

pd = dot(A, B)
print(pd)


'''
another way of doing this is 


A = [[12, 7, 3],
     [4, 5, 6],
     [7, 8, 9]]

B = [[5, 8, 1, 2],
     [6, 7, 3, 0],
     [4, 5, 9, 1]]

r = [[sum(a*b for a, b in zip(rA, cB)) // then create the product
 for cB in zip(*B) // column of the b and kind of transpose
 ] for rA in A // outer loop]
for row in r:
    print(row)
'''