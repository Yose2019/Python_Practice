'''
Write a getHoursMinutesSeconds() function that has a totalSeconds parameter. The 
argument for this parameter will be the number of seconds to be translated into the number of hours, 
minutes, and seconds. If the amount for the hours, minutes, or seconds is zero, don’t show it: the 
function should return '10m' rather than '0h 10m 0s'. The only exception is that 
getHoursMinutesSeconds(0) should return '0s'. 
These Python assert statements stop the program if their condition is False. Copy them to 
the bottom of your solution program. Your solution is correct if the following assert statements’ 
conditions are all True: 
assert getHoursMinutesSeconds(30) == '30s' 
assert getHoursMinutesSeconds(60) == '1m' 
assert getHoursMinutesSeconds(90) == '1m 30s' 
assert getHoursMinutesSeconds(3600) == '1h' 
assert getHoursMinutesSeconds(3601) == '1h 1s' 
assert getHoursMinutesSeconds(3661) == '1h 1m 1s' 
assert getHoursMinutesSeconds(90042) == '25h 42s' 
assert getHoursMinutesSeconds(0) == '0s' 
For an additional challenge, break up 24 hour periods into days with a ―d‖ suffix. For example, 
getHoursMinutesSeconds(90042) would return '1d 1h 42s'. 
'''

def getHoursMinutesSeconds(seconds):
    numOfSeconds = seconds % 60
    minutes = (seconds // 60) % 60
    hours = (seconds // (60 * 60))
    
    timeString = ''
    hourString = ''
    minuteString = ''
    secondString = ''

    if hours != 0:
        hourString = str(hours) + 'h'
    if minutes != 0:
        if hourString != '':
            minuteString = ' ' + str(minutes) + 'm'
        else:
            minuteString = str(minutes) + 'm'

    if seconds == 0 or numOfSeconds != 0:
        if minuteString != '' or hourString != '':
            secondString = ' ' + str(numOfSeconds) + 's'
        else :
            secondString = str(numOfSeconds) + 's'
        
    timeString = hourString + minuteString + secondString
    return timeString

    

assert getHoursMinutesSeconds(30) == '30s' 
assert getHoursMinutesSeconds(60) == '1m' 
assert getHoursMinutesSeconds(90) == '1m 30s' 
assert getHoursMinutesSeconds(3600) == '1h' 
assert getHoursMinutesSeconds(3601) == '1h 1s' 
assert getHoursMinutesSeconds(3661) == '1h 1m 1s' 
assert getHoursMinutesSeconds(90042) == '25h 42s' 
assert getHoursMinutesSeconds(0) == '0s' 