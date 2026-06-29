# find if the sting contains any special characters in it 

s = "#$%    Shristhi"

s2 = "Shristhi N Akkalkot"

def speCharIdentify(s):
    for i in s:
        if not i.isalnum() and not i.isspace(): 
            return True 
        
        return False 
    
print(speCharIdentify(s))
print(speCharIdentify(s2))