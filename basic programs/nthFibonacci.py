# Finding the nth fibonacci
# considering that first fibonacci number is 0 and the second is 1
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89......

def Fibonacci(nth:int):
    if nth==1 or nth==2:
        return nth-1
    else:
        n1 = 0
        n2 = 1
        for i in range(2, nth + 1):
            nfibo = n1 + n2
            n1 = n2
            n2 = nfibo

        return nfibo

# fibonacci by the formula reduces time and space complexity to O(1)
def FibonacciByFormula(nth:int):
    if nth<=0:
        raise ValueError("Input cannot be 0 or less")
    else:
        nfibo = (((1 + (5**0.5))**nth) - ((1 - (5**0.5))**nth)) / ((2**nth)*(5**0.5))
        return int(nfibo)


print(Fibonacci(11))
print(FibonacciByFormula(11))   