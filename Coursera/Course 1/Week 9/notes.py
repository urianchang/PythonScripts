#NOTES

counts = dict()
names = ["csev", "cwen", "csev", "zqian"]

for name in names : 
# Old way
#    if name not in counts:
#       counts[name] = 1
#    else :
#       counts[name] = counts[name] + 1
    
    counts[name] = counts.get(name, 0) + 1

print counts