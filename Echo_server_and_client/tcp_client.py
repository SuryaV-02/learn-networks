from http import client
import socket

clientFd = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
clientFd.connect(('localhost',55555))
message = input('Enter your Message to server : ')
clientFd.send(bytes(message,'utf-8'))
print(clientFd.recv(1024).decode())
