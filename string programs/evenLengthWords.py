# the program prints the even length words in the string 

s = "This is an example of the program which is mix\
    of even and odd lettered words"

# different methods are discussed in the same program 
words = s.split(" ")

lst = [word for word in words if len(word) % 2 == 0 and len(word) != 0]
new_str = " ".join(lst)
print(new_str)

# the brute force approach without using the in-built methods

words = []
empty_str = ""
for i in s:
    if i == " ":
        if len(empty_str) != 0 and len(empty_str) % 2 == 0:
            words.append(empty_str)

        empty_str = ""
        continue
    
    empty_str += i 

words = " ".join(words)
print(words)

