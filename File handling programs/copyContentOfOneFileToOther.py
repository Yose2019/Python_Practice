# program copies content of one file to another file
# this can be done by opening one file in read mode
# and the other in append mode

content = ""

with open(r"D:\practice\File handling programs\ex2.txt", 'r') as f_read:
    content = f_read.read()

with open(r"D:\practice\File handling programs\ex3.txt", 'a') as f_write:
    f_write.write(content)


