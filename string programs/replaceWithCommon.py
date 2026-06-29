# the program requires to replace all the occurences in the given list
# with a specific word 
# a constant reminder is that strings are immutable 

lst = ["ramen","sushi", "wasabi", "food", "macha"]

s = "Asian food is very popular these days, specially japanese. Food like ramen and sushi are popular worldwide. Even wasabi is popular these days along with macha"

const = "dumbo"

s = s.split(" ")

# s = " ".join(list(i for i in s if i not in lst else const))
s = " ".join([i if i not in lst else const for i in s])
# for i in range(len(s)):
#     if s[i] in lst:
#         s[i] = const 

# s = " ".join(s)
print(s)

