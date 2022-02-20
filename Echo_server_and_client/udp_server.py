import socket

serverfd = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

serverfd.bind(('localhost',55555))

while True:
    data,address = serverfd.recvfrom(1024)
    print('Client address : ',address)
    print('Client Message : ',data)
    serverfd.sendto(data,address)

