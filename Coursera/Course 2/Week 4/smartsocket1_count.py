import socket

user_url = raw_input("Enter URL: ")

try:
    host_name = user_url.split("/") [2]
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((host_name, 80))
    mysock.send('GET ' + user_url + ' HTTP/1.0\n\n')
except:
    print "!!Please enter a valid URL!!"
    
count = 0
while True:
    data = mysock.recv(512)
    count += len(data)
    if ( len(data) < 1 ) or count >= 3000 :
        break
    print data;

mysock.close()
print count
