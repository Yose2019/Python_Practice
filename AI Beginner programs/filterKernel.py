# the given program demonstrates the behaviour of filter kernel in the neural network (CNN)
# the program doesn't use the numpy module 
# this initial version has predefined / declared matrix for image and filter 
# the program is also currently only implemented for the 2-D images 

'''
Key points :
the dimesnsion of the resultant matrix are as follows 
- resultant = ((image - filter + 1) + ( 2 * padding )) / stride 

these are the crucial terms in the convolution phase 
''' 
from math import ceil

image = [
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5],
    [5, 7, 8, 9, 5],
    [3, 5, 7, 9, 5], 
    [1, 1, 1, 1, 1]
]

filter = [
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]
]

# the function or ( method ) creates the resultant matrix 
def res(imRow, imCol, filRow, filCol, padding, stride):
    colBound = ceil(((imCol - filCol + 1) + (2 * padding)) / stride) 
    rowBound = ceil(((imRow - filRow + 1) + (2 * padding)) / stride)
    return [[0 for i in range(0, int(colBound))] for i in range(0, int(rowBound)) ] 

# this is the main function
def conv(image, filter, padding, stride):
    # step one is to get the resultant matrix, it's dimensions
    # and also to get the image and filter dimensions 

    # dimensions of the image matrix 
    imRow = len(image); imCol = len(image[0]);
    filRow = len(filter); filCol = len(filter[0]);

    resMat = res(imRow, imCol, filRow, filCol, padding, stride)
    
    # get the dimensions of the resultant matrix 
    resRow = len(resMat); resCol = len(resMat[0]); 

    # now the main loop begins where the operation takes place 

    '''
    1. The structure of the loop is designed as such - the main loop running is while loop
    2. Whose condition depends on the resultant matrix dimension
    '''
    
    # initialising two variables which are tracking and used for entry into resultant matrix 
    rowSlide = 0; colSlide = 0;
    rowEntry = 0; colEntry = 0;

    while (rowEntry < resRow and colEntry < resCol):
         
        scalarValue = resMat[rowEntry][colEntry]

        # the bottle neck is filter kernel 
        for i in range(0, filRow):
            for j in range(0, filCol):
                scalarValue += image[i + rowSlide][j + colSlide] * filter[i][j]

        resMat[rowEntry][colEntry] = scalarValue 

        # now the crucial thing is updating the rowEntry and colEntry 
        colSlide += stride # updtae this equal to stride as the filter moves column wise first
        colEntry += 1 # the resultant matrix cannot be incremented by stride but only 1

        # now after all the columns are exhausted , the row gets incremented 
        if colEntry == resCol :
            colSlide = 0; colEntry = 0;
            rowSlide += stride; rowEntry += 1;

    return resMat
    
print(conv(image, filter, 0, 2))
