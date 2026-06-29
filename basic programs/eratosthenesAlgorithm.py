# -- sieve of eratosthenes is a classic algorithm used for checking prime numbers

# first obtain the lowest and the highest range 
# create a list whose index starts at zero and ends at the upper bound
# initialise the list with true 
# time complexity is O(nlogn)
# space complexity is O(n)

def eratosthenesAlgorithm(minimum:int, maximum:int):
    primes = [True for i in range(maximum+1)]
    primes[0] = primes[1] = False

    for i in range(2, (maximum//2)+1):
        if primes[i] == True:
            for j in range(i*i, maximum+1, i):
                primes[j] = False

    allPrimes = [i for i in range(minimum, maximum+1) if primes[i]]

    return allPrimes


print(eratosthenesAlgorithm(0,30))
