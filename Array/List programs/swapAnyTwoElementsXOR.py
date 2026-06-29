# swap any two elements by XOR 
# alternatively we can use methods like - arr[i], arr[j] = arr[j], arr[i] 
# or using a temporary variable 
# xor two numbers gets back the original number 
# 1011 ^ 1101 = 0110 
# 0110 ^ 1101 = 1011 

def swapByXOR(arr, i, j):

    arr[i] = arr[i] ^ arr[j] # 011 ^ 101 = 110 
    arr[j] = arr[i] ^ arr[j] # 110 ^ 101 = 011 
    arr[i] = arr[i] ^ arr[j] # 110 ^ 011 = 101 

    return arr 

print(swapByXOR([1,2,3,4,5], 1, 3))