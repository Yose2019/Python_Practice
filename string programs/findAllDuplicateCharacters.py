# the program returns all the duplicate elements in the string 

string = input("Enter the string : ")
char_set = set(string)
list_of_duplicates = []

list_of_duplicates = [i for i in char_set if string.count(i) > 1]

print(list_of_duplicates)

# an alternate way using the dictionary method 
def using_dictionary(string:str):
    char_dic = {}

    for i in string:
        char_dic[i] = char_dic.get(i, 0) + 1

    char_list = [i for i in char_dic.keys() if char_dic[i] > 1]

    return char_list 

print(using_dictionary(string))

    

