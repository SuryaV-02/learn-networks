from http import client
import socket

clientFd = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
clientFd.connect(('localhost',55555))

message = input('ENter your message : ')
clientFd.sendto(bytes(message,'utf-8'),('localhost',55555))
data,address = clientFd.recvfrom(1024)
print(address,' reply : ',data)