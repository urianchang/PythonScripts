# Week 5 Assignment: Extracting Data from XML

import urllib
import xml.etree.ElementTree as ET

url = raw_input('Enter URL: ')

# Open URL with urllib
print 'Retrieving', url
uh = urllib.urlopen(url)
data = uh.read()

# Retrieve the data
print 'Retrieved',len(data),'characters'

tree = ET.fromstring(data)
results = tree.findall('comments/comment')
print 'Comment count:', len(results)

# Count & add them up
c = 0
s = 0

for result in results :
    s = int(result.find('count').text) + s
    c = c + 1
    
print 'Count:', c
print 'Sum:', s