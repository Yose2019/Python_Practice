# the program requires to get the elements of all th rows in the kth column of the list

col = int(input("Enter the column number:"))
mat = [[4, 5, 6], 
     [8, 1, 10], 
      [7, 12, 5]]

if col >= len(mat[0]) :
    raise IndexError("Index out of range")
else :
    elements = [mat[i][col] for i in range(len(mat))]

'''
else we can also use the following 
elements = list(zip(*mat))[col]
'''

print(elements)