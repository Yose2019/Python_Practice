# array sum using divide and conquer method
# the time complexity is O(n) and space complexity is O(logn)

def arraySum(array, left, right):
    if array[left] == array[right]:
        return array[left]
    mid = (left + right)//2
    leftSum = arraySum(array, left, mid)
    rightSum = arraySum(array, mid+1, right)

    return leftSum + rightSum

print(arraySum([1,2,3,4], 0, 3))