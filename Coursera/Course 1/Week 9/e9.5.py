# Exercise 9.5

fname = raw_input("Enter the file name: ")
try :
    fhandle = open(fname, "r")
except :
    print "File cannot be opened:", fname
    exit()
    
domains = dict()
for line in fhandle : 
    line.strip
    if not line.startswith("From ") : continue
    words = line.split()
    email = words[1]
    domain = email.split("@")
    domains[domain[1]] = domains.get(domain[1],0) + 1
    
print domains