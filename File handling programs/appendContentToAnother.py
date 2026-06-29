# the program appends the content of one file to another file

f1 = r"D:\practice\File handling programs\ex2.txt"
f2 = r"D:\practice\File handling programs\ex3.txt"

# with open(f1, 'r') as f_read:
#     to_copy = f_read.read()

# with open(f2, 'a') as f_copy:
#     f_copy.write(to_copy + '\n')


# apart from the above method, we have the shutil module 
# the method name is called copyfileobj() 

import shutil

with open(f1, 'r') as file_to_be_copied, open(f2, 'a') as copied_to :
    shutil.copyfileobj(file_to_be_copied, copied_to)

