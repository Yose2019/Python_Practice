# given the 2 - d matrix of strings, concatenate to form a matrix 
# same column strings concatenated 

input = [["Gfg", "good"], ["is", "for"]]
output = []
for i in range(len(input[0])) :
    string = ""
    for j in range(len(input)) :
        string += input[j][i]

    output.append(string)

print(output)
    