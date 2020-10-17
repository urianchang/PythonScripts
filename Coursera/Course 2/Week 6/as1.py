import json
import urllib

#Prompt user for the URL
url = raw_input('Enter location: ')

#Retrieve URL
print 'Retrieving...', url
uh = urllib.urlopen(url)
data = uh.read()
print 'Retrieved',len(data),'characters!'

#Count and add them up!
count = 0
sum = 0

info = json.loads(str(data))
# print json.dumps(info, indent=4)

for item in info['comments'] :
    x = int(item['count'])
    sum = x + sum
    count = count + 1

print 'Sum:', sum
print 'Count:', count