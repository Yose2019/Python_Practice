# the program here counts the elements of the file 
# here the elements are characters, words, new lines, spaces 

# 1. This method tries to have a class with various operations in it
class fileOperations:
    def __init__(self, filePath:str):
        self.filePath = filePath 

    def countWords(self):
        words = 0
        with open(self.filePath, 'r') as f:
            for line in f:
                for word in line.split():
                    words += 1
        return words 
    
    def countLetters(self):
        letters = 0
        with open(self.filePath, 'r') as f:
            for ch in f.read():
                if ch.isalnum():
                    letters += 1
        return letters
    
    def countSpaces(self):
        spaces = 0
        with open(self.filePath, 'r') as f:
            for ch in f.read():
                if ch == " ":
                    spaces += 1
        return spaces
    
    def countNewline(self):
        newLine = 0
        with open(self.filePath, 'r') as f:
            for ch in f.read():
                if ch == '\n':
                    newLine += 1
        return newLine

    def countLines(self):
        lines = 0
        with open(self.filePath, 'r') as f:
            for line in f:
                lines += 1
        return lines

        

obj = fileOperations(r'D:\practice\File handling programs\ex2.txt')
print(obj.countLetters())
print(obj.countWords())
print(obj.countSpaces())
print(obj.countNewline())
print(obj.countLines())