# obtain two matrices where one is the sum and the other is the difference of the 
# given 2D matrices 

A = [[1,2],[3,4]]
B = [[4,5],[6,7]]

# using the brute force approach 

sum = [[0 for ele in A[0]] for ele1 in A]
diff = [[0 for ele in A[0]] for ele1 in A]

for row in range(len(A)):
    for col in range(len(A[0])):
        sum[row][col] = A[row][col] + B[row][col]
        diff[row][col] = A[row][col] - B[row][col]


print(sum)
print(diff)

'''
The program can also be done using numpy's add method 
and also using list coprehension and zip

sum = [[ a + b for a,b in zip(r1, r2)] for r1, r2 in zip(A,B)]

essentially the outer for loop will zip and form a pair for the respective row
row 1 of both A and B and so on, then respective elements of each row are zipped
'''
