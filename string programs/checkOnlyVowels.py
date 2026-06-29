# the program requires to print the word which contains all the vowels 
# it has to consist of all the vowels 'aeiou' in it 


def checkWord(word):
    word = word.lower()
    vowels = "aeiou"
    for i in vowels:
        if i not in word:
            return False 
        
    return True

# same logic as above using the all() function 
def checkWordUsingAll(word):
    word = word.lower()
    vowels = "aeiou"
    return all(v in word for v in vowels)

print(checkWord("aerodrumming"))
print(checkWord("random"))
print(checkWordUsingAll("aerodrumming"))
print(checkWordUsingAll("random"))


