# the program requires to find all the words whose length is greater than k 


l = int(input("Enter the variable k :"))
s = input("Enter the string : ")

s_new = " ".join(word for word in s.split(" ") if len(word) > l)

print(s_new)