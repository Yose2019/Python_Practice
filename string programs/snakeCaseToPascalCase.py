# convert the text in snake case to pascal case 
# snake case eg = this_is_snake_case
# pascal case eg = ThisIsPascalCase

# different methods are discussed in the program

def snakeToPascalCase1(s : str) -> str:
    s = s.split("_")
    temp = ""
    for word in s:
        temp += word.title()
    
    s = temp
    return s

def snakeToPascalCase2(s : str) -> str:
    s = "".join(word.capitalize() for word in s.split('_'))
    return s

print(snakeToPascalCase1('this_is_snake_case'))
print(snakeToPascalCase2("this_is_snake_case"))