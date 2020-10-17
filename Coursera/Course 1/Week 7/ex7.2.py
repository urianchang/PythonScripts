# Exercise 7.2

fname = raw_input("Enter the file name: ")

try :
    fhand = open(fname)
except : 
    print "Invalid file name"
    exit()

count = 0
total = 0

for line in fhand : 
    line = line.rstrip()
    if line.startswith("X-DSPAM-Confidence:") :
        sppos = line.find(" ")
        num = float(line[sppos+1:])
        total = total + num
        count = count + 1

avg = float(total/count)
print "Average spam confidence: ", avg


