# checking if a given a number is fibinacci number or not
# first of all use list / array
# then the limit is till those previous two numbers sum do not exceed the given number
# if they exceed then stop and return false
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

def checkFibonacci(num:int):
    fibo = [0, 1]
    while num >= fibo[-1] + fibo[-2]:
        fibo.append(fibo[-1]+fibo[-2])

    return num in fibo


print(checkFibonacci(21))
