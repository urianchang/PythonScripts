import urllib

user_url = raw_input("Enter URL: ")
html = urllib.urlopen(user_url).read()

print html