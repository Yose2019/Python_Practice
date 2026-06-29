# the program requires to reverse the words in a given string and 
# then change them in the same string 

filename = r"D:\practice\File handling programs\example.txt"

# this method uses readlines()
# with open(filename, 'r') as f:
#     lines = f.readlines()

# print(lines)
# lines[0] = lines[0].strip()
# lineOne = lines[0].split()[::-1]
# lines[0] = " ".join(lineOne) + '\n'


# with open(filename, 'w') as f:
#         f.writelines(lines)


# this method rather uses a bit more manual way 
# here it uses a for loop and a separate list which keeps on appending the lines
# although the logic remains the same 
# but internally it is a bit different 
lines = []
with open(filename, 'r') as f:
      for index, line in enumerate(f):
            line.strip('\n')
            if index == 0:
                line = line.split()[::-1]
                line = " ".join(line)
            
            lines.append(line + '\n')

with open(filename, 'w') as f:
      for line in lines:
            f.write(line)

