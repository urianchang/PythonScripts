
import urllib
from BeautifulSoup import *

url = raw_input('Enter URL: ')
html = urllib.urlopen(url).read()
print 'Retrieved', len(html), 'characters.'

# Parse HTML using BeautifulSoup
soup = BeautifulSoup(html)

#Retrieve tags
tags = soup('p')

#Count them up
c = 0
for tag in tags:
    c = c + 1

print 'Tag count:', c