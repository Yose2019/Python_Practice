# the program is used to find the character which occirs the maximum number of times

string = "the program is used to find the character which occirs the maximum number of times"

s = set(string)

char_dict = { c : string.count(c) for c in s}
print(char_dict)
char_dict = dict(sorted(char_dict.items(), key = lambda item : item[1], reverse=True))

print(next(iter(char_dict.items())))