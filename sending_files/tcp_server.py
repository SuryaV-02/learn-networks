import socket

serverFd = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serverFd.bind(('localhost',55555))
serverFd.listen(1)
download_file = open('download.txt','wb')

clientFd,address = serverFd.accept()
while True:
    data = clientFd.recv(1024)
    print('Retriving..')
    if(data ==b'END'):
        print('******')
        break
    download_file.write(data)
print('Data Written Successfully!')
download_file.close()
reply = bytes('File written','utf-8')
clientFd.send(reply)

