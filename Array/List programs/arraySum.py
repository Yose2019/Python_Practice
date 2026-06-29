# program to compute sum of elements in an array

def arraySum(array):
    sum = 0

    for i in array:
        if i != str(i):
            sum += i
        else:
            raise ValueError("Invalid type of data - only integer and float values are valid, String invalid")

    return sum

# one can also divide and conquer method but ideally this is optimum because
# time complexity is same O(n) 
# but space complexity is O(logn) for divide and conquer

print(arraySum([10,20,30,40,'50',60]))