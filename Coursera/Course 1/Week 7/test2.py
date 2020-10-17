# test

fname = raw_input("Enter the file name: ")

try :
    fhand = open(fname)
except : 
    print "Invalid file name"
    exit()

for line in fhand : 
    line = line.rstrip()
    if line.startswith("X-DSPAM-Confidence:") :
        sppos = line.find(" ")
        print sppos
        num = line[sppos+1:]
        print num
