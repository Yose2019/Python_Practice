'''
Write a program that displays the time for every 15 minute interval from 12:00 am to 11:45 pm. 
Your solution should produce the following output: 
12:00 am 
12:15 am 
12:30 am 
12:45 am 
1:00 am 
1:15 am --cut-- 
11:30 pm 
11:45 pm 
There are 96 lines in the full output. 
Try to write a solution based on the information in this description. If you still have trouble 
solving this exercise, read the Solution Design and Special Cases and Gotchas sections for 
additional hints. 
'''
# first try printing every 15 minutes 

for i in range(25):
    for j in range(0, 61, 15):
        if i//12 == 0:


