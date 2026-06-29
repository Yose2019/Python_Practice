# the program merges numerous files into single file 

files = []
while True:
    filepath = input("Enter the path of the file which is to be merged or enter stop to stop:")
    if filepath == "stop":
        break
    files.append(filepath)

with open(r"D:\practice\File handling programs\merged.txt","w") as newMergedFile:
    for file in files:
        with open(file, 'r') as fileUnderProcess:
            newMergedFile.write(fileUnderProcess.read())

'''
in this we can additionally check whether the file ends with '\n'
else in the case it is absent then we can append it 
'''


