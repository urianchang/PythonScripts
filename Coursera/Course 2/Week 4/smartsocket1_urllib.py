import urllib

user_url = raw_input("Enter URL: ")

try:
    html = urllib.urlopen(user_url).read()
except:
    print "!!Please enter a valid URL!!"
    
count = 0
while True:
    count += len(html)
    if ( len(html) < 1 ) or count >= 3000 :
        break

print html;
print "count is:", count
