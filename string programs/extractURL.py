# the program discuses method to extract URL from the string 

# the program uses the given lgic that - the url must start from https
# and the url doesn't contain any spaces 

s = "My Profile: https://www.geeksforgeeks.org/404.html/ in the portal of https://www.geeksforgeeks.org/"

# split at spaces 
urls =[i for i in s.split(" ") if i.startswith("https")]

print(urls)