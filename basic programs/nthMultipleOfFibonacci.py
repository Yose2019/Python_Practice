# compute the nth multiple of a given fibonacci number

def nthMultipleOfFibonacci(nth:int, num:int):
    fibo = [0, 1]
    count = 0
    while True:
        if (fibo[-1] + fibo[-2]) % num == 0:
            count+=1
            if count == nth:
                return fibo[-1] + fibo [-2]
        fibo.append(fibo[-1] + fibo[-2])

print(nthMultipleOfFibonacci(2,3))

# alternatively using an approach which reduces the space overhead
nth = int(input("Enter the nth multiple:"))
num = int(input("Enter the number:"))
a, b = 0, 1
count = 0
while True:
    a, b = b, a+b
    
    if b % num == 0:
        count += 1
        if count == nth:
            print(b)
            break


