
import urllib
from BeautifulSoup import *

url = raw_input('Enter URL: ')

count = int(raw_input('Enter count: '))
position = int(raw_input('Enter position: ')) - 1
urllist = list()
urllist.append(url)

# This is position #1
print 'Retrieving the initial URL:', urllist[0]

# Create loop to open URL
for x in range(count):
    html = urllib.urlopen(url).read()
# Parse HTML using BeautifulSoup
    soup = BeautifulSoup(html)
#Retrieve tags
    tags = soup('a')
    taglist = list()
    for tag in tags:
# Look at the parts of a tag
        # print 'TAG:',tag
        # print 'URL:',tag.get('href', None)
        # print 'Contents:',tag.contents[0]
        taglist.append(tag)
    url = taglist[position].get('href', None)
    print 'Retrieving:', url
    urllist.append(url)

lasturl = urllist[-1]
breakurl = str(lasturl).split("/")
lastpos = breakurl[7].split("_")
remext = lastpos[-1].split(".")
lastname = remext[0]

print 'Last URL:', lasturl
print 'Last name:', lastname
