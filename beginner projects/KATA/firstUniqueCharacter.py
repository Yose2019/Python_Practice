'''
the program finds the first unique character which appears once
'''

def first_unique_character(word: str):
    '''
    the function finds the first unique character 
    '''
    word = word.strip()

    if word == "":
        raise ValueError("Empty string - no characters present")

    if len(word) == 1:
        return word 

    character_dict = {}

    for chr in word:
        character_dict[chr] = character_dict.setdefault(chr, 0) + 1

    if 1 not in character_dict.values():
        raise ValueError("No unique characters are present")

    for key, value in character_dict.items():
        if value == 1:
            return key 

def main():
    try:
        word = input("Enter the word: ")
        print(f"The unique character is : {first_unique_character(word)}")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()




