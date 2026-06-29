# this method trial division is useful for checking a single prime number
# time complexity is O((n)**(1/2))
# space complexity is O(n)
# this is based on the following theory => n = (aXb) for composite number
# thus , the numbers are such that , a = b = (n**0.5)
# or either a or b is less that (n**0.5)

def trialDivision(num:int):
    if num <= 1:
        return False
    
    if num == 2:
        return True

    for i in range(2, int(num**(0.5))+1):
        if num%i == 0:
            return False
        
    return True

# alterntively can also use this
# check one condition initially with num%2 , as all even numbers are numtiples of two
# then in range , check using only odd numbers by starting from 3 and skipping by 2
# for i in range(3, (int(num**0.5)+1), 2)

primes = [i for i in range(20) if trialDivision(i)]
print(primes)

     