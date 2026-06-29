# generate all permutations of a string 
# 'ABC', 'ACB', 'BCA', 'BAC', 'CBA' , 'CAB'.....

# the following is implemented via a permutation 

# credits for solution - gfg 


#  if main string is empty, print it 
def permute(s, s2):
    if len(s) == 0:
        print(s2, end=' ')
        return
    
    for i in range(len(s)):
        char = s[i]
        left_s = s[0:i]
        right_s = s[i+1:]
        rest = left_s + right_s
        permute(rest, s2 + char)

s1 = "ABC"
s2 = ""
permute(s1, s2)