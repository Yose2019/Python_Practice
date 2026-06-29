# this program finds the length of string :) 
# different methods are discussed in the same program :)

def inbuiltFunc(s):
    print(len(s))

def usingCount(s):

    count = 0
    for i in s:
        count += 1

    print(count)

inbuiltFunc("applevada")
usingCount("batatavada")