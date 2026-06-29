# the program requires to split at spaces and join at the delimeters which are given as input 

# brute force method and the standard methods are discussed 

def bruteForce(s:str, delmtr:str) -> str:

    words = []
    word = ""

    for chr in s:
        if chr == " ":
            words.append(word)
            word = ""
            continue 
        word += chr 

    words.append(word)

    ret = ""
    for word in words[:len(words) - 1]:
        ret += (word + delmtr)

    ret += words[len(words) - 1]

    return ret 

# using the inbuilt methods 

def splitAndJoin(s:str, delmtr:str) -> str:
    return delmtr.join(s.split(" "))

print(bruteForce("Hello, how are you?", "-"))
print(splitAndJoin("Hello, how are you?", "-"))

