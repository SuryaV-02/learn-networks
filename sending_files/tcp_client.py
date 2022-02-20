from distutils.command.upload import upload
from http import client
import socket

clientFd = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
clientFd.connect(('localhost',55555))

upload_file = open('upload.txt','rb')
while True:
    data = upload_file.read(1024)
    print(data)
    if(data ==b'END'):
        print('#####')
        break
    clientFd.send(data)

reply,address = clientFd.recv(1024).decode()
print(address,' : ',reply)