import socket

serverFd = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

SERVER_ADDRESS = ('localhost',55555)
serverFd.bind(SERVER_ADDRESS)
serverFd.listen(99)

print('Server up..')
while True:
    clientFd,address = serverFd.accept()
    client_message = clientFd.recv(1024).decode()
    print('--> ',address,client_message)
    reply = input('<-- ',)
    if(reply=='END'):
        print('Server down..')
        break
    clientFd.send(bytes(reply,'utf-8'))