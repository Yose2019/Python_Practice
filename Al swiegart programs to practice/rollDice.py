'''
Write a rollDice() function with a numberOfDice parameter that represents the number of 
six-sided dice. The function returns the sum of all of the dice rolls. For this exercise you must import 
Python’s random module to call its random.randint() function for this exercise. 
These Python assert statements stop the program if their condition is False. Copy them to 
the bottom of your solution program. Your solution is correct if the following assert statements’ 
conditions are all True. We can’t predict rollDice()’s random return value, but we can do 
repeated checks that the return value is within the correct range of expected values: 
assert rollDice(0) == 0 
assert rollDice(1000) != rollDice(1000) 
for i in range(1000): 
assert 1 <= rollDice(1) <= 6 
assert 2 <= rollDice(2) <= 12 
assert 3 <= rollDice(3) <= 18 
assert 100 <= rollDice(100) <= 600 
There is an astronomically small chance that the assert rollDice(1000) != 
rollDice(1000) will fail with a false positive. This assertion tests that rollDice() doesn’t 
simply return the same ―random‖ number each time by simulating rolling 1,000 dice twice and making 
sure the totals are different for both rolls. But, of course, there is a chance they’ll come up the same 
total and cause an AssertionError. In that case, just rerun the assertion tests. After all, what are 
the odds of that happening twice? 
Try to write a solution based on the information in this description. If you still have trouble 
solving this exercise, read the Solution Design and Special Cases and Gotchas sections for 
additional hints. 
'''

from random import randint as ri 

def rollDice(num):
    if num == 0:
        return 0
    
    diceRollSum = 0
    
    while num != 0:
        diceRollSum += ri(1, 6)
        num -= 1

    return diceRollSum

assert rollDice(0) == 0 
assert rollDice(1000) != rollDice(1000) 
for i in range(1000): 
    assert 1 <= rollDice(1) <= 6 
    assert 2 <= rollDice(2) <= 12 
    assert 3 <= rollDice(3) <= 18 
    assert 100 <= rollDice(100) <= 600 
