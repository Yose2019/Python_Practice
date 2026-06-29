# The program contains two lists
# one list contains integers and based on that the second list neads to rearranged 

arr = ['a', 'c', 'v', 'h']
num = [12, 45, 21, 34]

num2 = sorted(num)

if len(arr) != len(num) :
    raise ValueError("The length of the lists must be same")
else:
    lst = []
    for i in num2:
        lst.append(arr[num.index(i)])
print(lst)
