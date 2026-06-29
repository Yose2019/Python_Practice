import random, sumAndProduct 
numbers = [] 
for i in range(100): 
    numbers.append(random.randint(1, 1000000000)) 
print('Numbers:', numbers) 
print('    Sum is', sumAndProduct.calculateSum(numbers)) 
print('Product is', sumAndProduct.calculateProduct(numbers))