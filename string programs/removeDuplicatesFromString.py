# the program requires to remove duplicates from the string 

s = "alphaba"
no_duplicates = ""

for i in s : 
    if i.lower() not in no_duplicates:
        no_duplicates += i.lower()


print(no_duplicates)