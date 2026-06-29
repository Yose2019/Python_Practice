#finding the simple interest 
def findSimpleInterest(principle, rateOfInterest, time, timeFormat:str='y'):
    if timeFormat.lower() == 'y':
        return round((principle*rateOfInterest*time)/100,2)
    elif timeFormat.lower() == 'm':
        return round((principle*rateOfInterest*(time/12))/100,2)
    elif timeFormat.lower() == 'd':
        return round((principle*rateOfInterest*((time/365)))/100,2)
    
print(findSimpleInterest(10000,2,24,'d'))

