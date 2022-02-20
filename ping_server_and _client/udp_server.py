import socket

serverFd = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
serverFd.bind(('localhost',55555))
print('Server ready and up..')

while True:
    data,address = serverFd.recvfrom(1024)
    print('Received ',data,' from ',address)
    serverFd.sendto(data,address)
    