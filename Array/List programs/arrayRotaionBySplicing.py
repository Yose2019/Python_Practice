# similar to array rotation by reversing the sub - arrays 
# here we use the splicing 

def arrayRotationBySplicing(arr, shift:int):
    arr = arr[shift:] + arr[:shift]
    return arr

print(arrayRotationBySplicing([2,3,4,5,6,7,8,9], -5))

