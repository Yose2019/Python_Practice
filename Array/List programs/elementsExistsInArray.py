# this program discusses various methods which is used to check
# whether an element exists in an array or not 

'''
1. The first method uses the 'in' to check whether an elements is present 
'''
def findUsingIn(arr, ele):
    if ele in arr:
        return True 
    else:
        return False 
    
'''
2. Using any function 
works on iterables 
[True, False, False] return True with any function as Truthy

(function_call(expression for item in iterable))
general form for doing generator exprssion 

this is more efficient in cases as whe it approaches a True value early it stops and returns true
'''
def findUsingAny(arr, ele):
    return any(i == ele for i in arr) 

'''
3. Using the count function 
'''
def findUsingCount(arr, ele):
    if arr.count(ele) > 0:
        return True
    else:
        return False 
    
'''
4.Find using one pass through the arr 
'''
def findUsingPass(arr, ele):
    flag = False 

    for i in arr:
        if i == ele:
            flag = True 
            break 

    return flag 

'''
5. Attempting using a binary search 
'''
def findUsingBinarySearch(arr, ele):
    ans = False 

    left = 0; right = len(arr) - 1;

    while(left <= right):
        mid = (left + right) // 2
        if arr[mid] == ele:
            ans = True 
            break 
        if arr[mid] < ele:
            left = mid + 1
        else:
            right = mid  

    return ans 

arr = [1,2,3,4,5,6,7]
print(findUsingIn(arr,2))
print(findUsingAny(arr, 32))
print(findUsingCount(arr,5))
print(findUsingPass(arr,9))
print(findUsingBinarySearch(arr,34))
print(findUsingBinarySearch(arr,3))
