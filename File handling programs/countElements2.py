# the program has the same elements as 'countElements' program 
# the approach has been modified 

def countElements(fileName):
    lines = spaces = words = letters = 0

    with open(fileName, 'r') as f:
        for line in f:
            lines += 1
            spaces += line.count(" ")
            words += len(line.split())
            letters += sum(len(x) for x in line.split())
            

        print("lines:",lines,"spaces:",spaces,"words:",words,"letters:",letters)

fileName = r"D:\practice\File handling programs\ex3.txt"
countElements(fileName)



