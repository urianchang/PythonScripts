
import urllib
from BeautifulSoup import *

url = raw_input('Enter URL: ')
html = urllib.urlopen(url).read()

# Parse HTML using BeautifulSoup
soup = BeautifulSoup(html)

#Retrieve tags
tags = soup('span')

#Count them up
c = 0
s = 0
for tag in tags:
   # Look at the parts of a tag
   # print 'TAG:',tag
   # print 'Contents:',tag.contents[0]
   s = int(tag.contents[0]) + s
   c = c + 1

print "COUNT:", c
print "SUM:", s

