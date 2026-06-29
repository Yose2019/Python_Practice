# given any array we need to rotate the array 
# there are many methods which can be explored 
# first let us discuss the classic method of reversal and then rotate


#consider we are performing the 
def arrayRotationByReversal(arr, shift:int):
    arr[:shift] = reversed(arr[:shift])
    arr[shift:] = reversed(arr[shift:])

    arr.reverse()
    return arr

print(arrayRotationByReversal([1,2,3,4,5,6,7,8], 2)) 

