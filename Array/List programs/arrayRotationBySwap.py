# this is similar to reversal but instead of using the reverse function 
# we using swapping to reverse the segment of array

def arrayRotationBySwap(arr, shift:int):
    start = 0; end = len(arr);

    for i in range(start, shift//2):
        arr[i], arr[shift - i - 1] = arr[shift - i - 1], arr[i]

    for i in range(shift, end//2):
        arr[i], arr[end - i - 1] = arr[end - i - 1], arr[i]

    for i in range(start, end//2):
        arr[i], arr[end - i - 1] = arr[end - i - 1], arr[i]

    return arr

'''
-- another method of doing this swap is by using while loop 
-- we can use while loop to do the same
-- essentially start and end condition remain the same
start, end = 0, shift-1
while start < end :
arr[start], arr[end] = arr[end], arr[start]
start += 1
end -= 1

start, end = shift, len(arr) - 1
while start < end :
arr[start], arr[end] = arr[end], arr[start]
start += 1
end -= 1

-- rotate the whole array
start, end = 0, len(arr) - 1
while start < end :
srr[start], arr[end] = arr[end], arr[start]
start += 1
end -= 1

'''
print(arrayRotationBySwap([1,2,3,4,5,6,7,8], 2))
    