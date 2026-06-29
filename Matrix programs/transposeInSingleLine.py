# this program deals with transposing a matric in single line 

# instead of brute force
# brute force will also be discussed 

A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

tranA = list(ele for ele in zip(*A))
print(tranA)

# the same we can do by running two loops 

tran2 = [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]

print(tran2)