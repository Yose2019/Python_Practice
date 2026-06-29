def replaceWithOther(string:str, to_be_replaced:str, replaced_with:str):
    while string.find(to_be_replaced) != -1:
        string = string.replace(to_be_replaced, replaced_with)

    return string

print(replaceWithOther("python java python cpp python", "python", "c"))