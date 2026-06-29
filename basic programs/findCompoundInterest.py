# --find compound interest---


def compoundInterestAmount(principle, rate, time, timeFormat:str):
    if timeFormat == 'y':
        return principle * ((1 + rate/100)**time) 
    elif timeFormat == 'm':
        return principle * ((1 + rate/100)**(time/12))
    elif timeFormat == 'd':
        return principle * ((1 + rate/100)**(time/365))
    elif timeFormat not in ['y','m','d']:
        raise ValueError("Invalid paramter for timeFormat")
        
        
def compoundInterest(principle, rate, time, timeFormat:str = 'y'):
    return round(compoundInterestAmount(principle, rate, time, timeFormat.lower()) - principle, 2)

print(compoundInterest(1000,3,10,'a'))