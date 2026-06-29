# program to add two matrices 
# different methods are discussed in the same program 

# 1. using list comprehension
def addMatrices(mat1, mat2): 
    add = [[mat1[i][j] + mat2[i][j] for i in range(len(mat1[0]))] for j in range(len(mat1))]
    print(add)

    
# 2. Using nested loops
def addMatricesUsingNestedLoops(mat1, mat2):
    add = [[],[],[]]
    for i in range(len(mat1)):
        for j in range(len(mat1[0])):
            add[i].append(mat1[i][j] + mat2[i][j])

    print(add)


    
a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
b = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
    
addMatricesUsingNestedLoops(a, b)
addMatrices(a, b)



