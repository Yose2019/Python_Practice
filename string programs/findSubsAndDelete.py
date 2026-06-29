# recursively find the substring in the main string and delete it 

string = "aaaaaa"
sub_string = "aa"

while string.find(sub_string) != -1:
    string = string.replace(sub_string, "")

if string == "":
    print("Yes it is possible")
else:
    print("No it is not possible")