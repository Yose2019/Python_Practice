# this is used to multiply an image matrix with the filter kernel matrix 
# this is the complete beginner interpretation 
# initially this version doesn't consider the addition of padding 
# the formula to get the dimension of resultant matrix is as follows 
# n = ((main_dimension - filter_dimension + (2*padding))/stride) + 1

# let us consider stride of 1 ideally 

'''
Algorithm : 
1. The filter kernel is constant - it doesn't change over the runtime when assigned once 
2. The matrix chosen is multiplied and the scalar product is obtained 
3. For multiplication and addition, we can use sep function or same 
4. Then based on the stride, we need to move the window, with considering edge cases 
5. We can use the size of the filter matrix to adjust and isolate from the image matrix
6. 
'''

image = [
    [1, 9, 1, 5, 0],
    [9, 10, 5, 1, 3],
    [3, 5, 7, 9, 1],
    [0, 5, 1, 1, 9],
    [2, 1, 2, 8, 1]
]

filter = [
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]
]

def resultant_matrix(rowImage, colImage, rowFilter, colFilter, stride, padding):
    r_row = ((rowImage - rowFilter + (2 * padding))//stride) + 1 
    r_col = ((colImage - colFilter + (2 * padding ))//stride) + 1

    return [[0 for i in range(r_col)] for j in range(r_row)]

def multiplication_and_add(image, filter):
    begin_row = 0; begin_col = 0; # by default the rows and columns begin at zero

    # get the dimensions of the matrices 
    imageRows = len(image); imageCols = len(image[0]);
    filterRows = len(filter); filterCols = len(filter[0]); 

    res = resultant_matrix(imageRows, imageCols, filterRows, filterCols, 1, 0)

    # now we need to make sure to fill the matrix 
    resRow = 0; resCol = 0; 

    while (begin_col + filterCols < imageCols or begin_row + filterRows < imageRows) : # this is the main loop 

        # run the for loops 
        scalarValue = res[resRow][resCol] # set the value to the resultant matrix value

        for i in range(begin_row, begin_row + filterRows):
            for j in range(begin_col, begin_col + filterCols):
                scalarValue += (image[i][j] * filter[i - begin_row][j - begin_col])

        # append / replace the obtaind value in resultant matrix and 
        # increment the values accordingly
        res[resRow][resCol] = scalarValue


    #     '''
    #     1. How to increment? 
    #     2. First priority is col and increment is equal to stride, 
    #     3. Col is incremented till the begin_col + filter_cols < images_cols 
    #     4. if condition three is met, begin_rows is incremented while
    #     the cols are set back to 0 and the 2, 3 is continued 
    #     5. If incase both are met with the exhaustive condition, then the loop gets terminated 
    #     6. Then the result get incremented within the above condition  
    #     '''
        if begin_col + filterCols < imageCols : 
            begin_col += 1; 
            resCol += 1;
        elif begin_row + filterRows < imageRows:
            begin_col = 0; begin_row += 1;
            resRow += 1; resCol = 0;
        

    print(res)


multiplication_and_add(image, filter)


                




