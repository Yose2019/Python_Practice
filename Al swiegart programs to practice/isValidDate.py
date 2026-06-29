'''
Write an isValidDate() function with parameters year, month, and day. The function 
should return True if the integers provided for these parameters represent a valid date. Otherwise, 
the function returns False. Months are represented by the integers 1 (for January) to 12 (for 
December) and days are represented by integers 1 up to 28, 29, 30, or 31 depending on the month 
and year. Your solution should import your leapyear.py program from Exercise #20 for its 
isLeapYear() function, as February 29th is a valid date on leap years. 
September, April, June, and November have 30 days. The rest have 31, except February which 
has 28 days. On leap years, February has 29 days. 
These Python assert statements stop the program if their condition is False. Copy them to 
the bottom of your solution program. Your solution is correct if the following assert statements’ 
conditions are all True: 
assert isValidDate(1999, 12, 31) == True 
assert isValidDate(2000, 2, 29) == True 
assert isValidDate(2001, 2, 29) == False 
assert isValidDate(2029, 13, 1) == False 
assert isValidDate(1000000, 1, 1) == True 
assert isValidDate(2015, 4, 31) == False 
assert isValidDate(1970, 5, 99) == False 
assert isValidDate(1981, 0, 3) == False 
assert isValidDate(1666, 4, 0) == False 
import datetime 
d = datetime.date(1970, 1, 1) 
oneDay = datetime.timedelta(days=1) 
65 
Python Programming Exercises, Gently Explained 
for i in range(1000000): 
assert isValidDate(d.year, d.month, d.day) == True 
d += oneDay
'''

import leapYear

def isValidDate(year, month, day):
    isLeapYear = False 
    if year < 0:
        return False 
    if leapYear.isLeapYear(year):
        isLeapYear = True 

    if month > 12 or month < 1 :
        return False 
    
    validDays = 0
    
    if month == 2 and isLeapYear :
        validDays = 29
    elif month == 2 and not isLeapYear : 
        validDays = 28
    elif month < 8:
        if month % 2 == 0:
            validDays = 30
        else:
            validDays = 31
    elif month >= 8:
        if month % 2 == 0:
            validDays = 31
        else:
            validDays = 30 
    if day > validDays or day <= 0:
        return False 
    
    return True 

assert isValidDate(1999, 12, 31) == True 
assert isValidDate(2000, 2, 29) == True 
assert isValidDate(2001, 2, 29) == False 
assert isValidDate(2029, 13, 1) == False 
assert isValidDate(1000000, 1, 1) == True 
assert isValidDate(2015, 4, 31) == False 
assert isValidDate(1970, 5, 99) == False 
assert isValidDate(1981, 0, 3) == False 
assert isValidDate(1666, 4, 0) == False 
import datetime 
d = datetime.date(1970, 1, 1) 
oneDay = datetime.timedelta(days=1) 
for i in range(1000000): 
    assert isValidDate(d.year, d.month, d.day) == True 
    d += oneDay 


