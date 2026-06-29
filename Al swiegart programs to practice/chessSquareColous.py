'''
Write a getChessSquareColor() function that has parameters column and row. The 
function either returns 'black' or 'white' depending on the color at the specified column and 
row. Chess boards are 8 x 8 spaces in size, and the columns and rows in this program begin at 0 and 
end at 7 like in Figure 9-1. If the arguments for column or row are outside the 0 to 7 range, the 
function returns a blank string. 
'''

def getChessSquareColor(row, column):
    if (row <= 8 and row >= 1) and (column <= 8 and column >= 1):
        row -=1 
        column -= 1 
        # if (row % 2 == 0 and column % 2 == 1) or (row % 2 == 1 and column % 2 == 0):
        #     return 'black'
        # else:
        #     return 'white'
        if (row + column) % 2 == 0:
            return 'white'
        else:
            return 'black'
    return ''
    

assert getChessSquareColor(1, 1) == 'white' 
assert getChessSquareColor(2, 1) == 'black' 
assert getChessSquareColor(1, 2) == 'black' 
assert getChessSquareColor(8, 8) == 'white' 
assert getChessSquareColor(0, 8) == '' 
assert getChessSquareColor(2, 9) == '' 