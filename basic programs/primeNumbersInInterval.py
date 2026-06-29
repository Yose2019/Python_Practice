# -- print all prime numbers in an interval

def checkPrime(num:int):
    if num==2:
        return True
    for i in range(2,(num//2)+1):
        if num%i == 0:
            return False
        
    return True

def primeNumbersInInterval(start:int, stop:int):
    if start == 1:
        start += 1
    for i in range(start, stop+1):
        if (checkPrime(i) == True):
            print(i,end=",")


primeNumbersInInterval(7,13)