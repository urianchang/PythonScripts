# Exercise 10.1

fname = raw_input("Enter the file name: ")
try :
    fhandle = open(fname, "r")
except :
    print "File cannot be opened:", fname
    exit()
    
emails = dict()
for line in fhandle :
    line.strip()
    if not line.startswith("From ") : continue
    email = line.split()
    emails[email[1]] = emails.get(email[1], 0) + 1

lst = list()
for email, count in emails.items() :
    lst.append( (count, email) )
    
lst.sort(reverse=True) 

for count, email in lst[:1] :
    print email, count