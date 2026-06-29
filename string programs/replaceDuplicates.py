# the program essentially implements the replacement of duplicates with pre-defined pronouns or replacements 

# consider the replacement words are defined in a dictionary 

s = "Gfg is best. Gfg also has Classes now. Classes help understand better." 

rep = {"Gfg":"It", "Classes":"They"}

# for implementation
# split the string into list 
s = s.split(" ")
# iterate using an iterator over the list 
# keep a set which adds the new ones and if already in list replaces it 
st = set()
for i in range(len(s)):
    if s[i] not in st:
        st.add(s[i])
    else:
        s[i] = rep[s[i]]

s = " ".join(s)

print(s)
