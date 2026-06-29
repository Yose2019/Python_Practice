'''
Write a function named getCostOfCoffee() that has a parameters named 
numberOfCoffees and pricePerCoffee. Given this information, the function returns the total 
cost of the coffee order. This is not a simple multiplication of cost and quantity, however, because the 
coffee shop has an offer where you get one free coffee for every eight coffees you buy. 
For example, buying eight coffees for $2.50 each costs $20 (or 8 × 2.5). But buying nine coffees 
also costs $20, since the first eight makes the ninth coffee free. Buying ten coffees calculates as 
follows: $20 for the first eight coffees, a free ninth coffee, and $2.50 for the tenth coffee for a total of 
$22.50. 
These Python assert statements stop the program if their condition is False. Copy them to 
the bottom of your solution program. Your solution is correct if the following assert statements’ 
conditions are all True: 
assert getCostOfCoffee(7, 2.50) == 17.50 
assert getCostOfCoffee(8, 2.50) == 20 
assert getCostOfCoffee(9, 2.50) == 20 
assert getCostOfCoffee(10, 2.50) == 22.50 
for i in range(1, 4): 
assert getCostOfCoffee(0, i) == 0 
assert getCostOfCoffee(8, i) == 8 * i 
assert getCostOfCoffee(9, i) == 8 * i 
assert getCostOfCoffee(18, i) == 16 * i 
assert getCostOfCoffee(19, i) == 17 * i 
assert getCostOfCoffee(30, i) == 27 * i 

'''

def getCostOfCoffee(numberOfCoffee, cost):
    if numberOfCoffee > 8:
        return (numberOfCoffee - (numberOfCoffee // 8)) * cost 
    else :
        return numberOfCoffee * cost 
    # to avoid the if-else conditioning we can use the //9 instead of 8 
    

assert getCostOfCoffee(7, 2.50) == 17.50 
assert getCostOfCoffee(8, 2.50) == 20 
assert getCostOfCoffee(9, 2.50) == 20 
assert getCostOfCoffee(10, 2.50) == 22.50 
for i in range(1, 4): 
    assert getCostOfCoffee(0, i) == 0 
    assert getCostOfCoffee(8, i) == 8 * i 
    assert getCostOfCoffee(9, i) == 8 * i 
    assert getCostOfCoffee(18, i) == 16 * i 
    assert getCostOfCoffee(19, i) == 17 * i 
    assert getCostOfCoffee(30, i) == 27 * i 