# factorial of a number

def factorial(num:int):
    fact = 1
    if num==0:
        return 1
    while num != 0:
        fact *= num
        num -= 1

    return fact


print(factorial(1))

# alternatively math module has an import function 
# math module allows us to use math.factorial()