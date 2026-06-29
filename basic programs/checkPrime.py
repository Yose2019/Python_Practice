# -- checking the prime numbers --

def checkPrime(num:int):
    if num==0 or num==1:
        return False
    if num==2:
        return True
    for i in range(2,(num//2)+1):
        if num%i == 0:
            return False
        
    return True

for i in range(21):
    if (checkPrime(i)):
        print(f"{i}:Prime")
    else:
        print(f"{i}:not Prime")