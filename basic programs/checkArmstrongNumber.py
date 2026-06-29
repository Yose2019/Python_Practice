# checking the armstrong number

def countDigits(num:int):
    numDigits = 0
    while num != 0:
        num //= 10
        numDigits += 1
    return numDigits

def checkArmstrong(num:int):
    numDigits = countDigits(num)
    numGen = 0
    while num != 0:
        numGen += (num%10)**(numDigits)
        num //= 10
    return numGen

checkNumber = int(input())
if checkNumber == checkArmstrong(checkNumber):
    print("Armstrong")
else:
    print("Not armstrong")
