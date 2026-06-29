# the program finds all the characters hich occur the minimum number of times in the string

s = "alphaba"

d = { i : s.count(i) for i in s}
mn = min(d.values())

for key, value in d.items():
    if value == mn:
        print(key, sep = "\t")