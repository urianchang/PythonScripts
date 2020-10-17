# Assignment 7.2

fname = raw_input("Enter file name: ")
fh = open(fname)

count = 0
total = 0

for line in fh : 
    line = line.rstrip()
    if not line.startswith("X-DSPAM-Confidence:") : continue
    spos = line.find(" ")
    num = float(line[spos+1:])
    total = total + num
    count = count + 1    

avg = total/count
print "Average spam confidence:", avg