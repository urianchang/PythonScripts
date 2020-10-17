# Exercise 9.4

fname = raw_input("Enter the file name: ")
try :
    fhandle = open(fname, "r")
except :
    print "File cannot be opened:", fname
    exit()
    
emails = dict()
for line in fhandle : 
    line.strip
    if not line.startswith("From ") : continue
    email = line.split()
    emails[email[1]] = emails.get(email[1], 0) + 1

bigcount = None
bigemail = None
for email,count in emails.items() : 
    if bigcount is None or count > bigcount:
        bigemail = email
        bigcount = count

print bigemail, bigcount