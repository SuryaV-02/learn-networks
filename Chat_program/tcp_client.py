import socket

clientFd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientFd.connect(('localhost',55555))
print('Logged in..')
while True:
    chat_message = input('<-- ')
    if(chat_message == 'END'):
        print('Logged out.')
        break
    clientFd.send(bytes(chat_message,'utf-8'))
    reply= clientFd.recv(1024).decode()
    print('--> ',reply)