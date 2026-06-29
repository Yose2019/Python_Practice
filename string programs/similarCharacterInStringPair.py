# check and find the number of similar of similar characters
# in a given pair of non-identical strings 

s1 = "apple"
s2 = "grape"

# convert then into a set 
s1 = set(s1)
s2 = set(s2)

print(s1, s2) 

count = 0 

for i in s1:
    if i in s2:
        count += 1

count_intersection = len(s1.intersection(s2))
count_intersection_by_operator = len(s1 & s2)

print(count)
print(count_intersection)
print(count_intersection_by_operator)