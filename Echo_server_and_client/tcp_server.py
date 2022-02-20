import socket

socketfd = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

socketfd.bind(('localhost',55555))
socketfd.listen(3)
print('waiting for connnections..')

while True:
    clientfd,addr = socketfd.accept()
    receivedMsg = clientfd.recv(1024).decode()
    replyMessage = 'ACK ' + receivedMsg
    print('Client Address : ',addr)
    print('Client message : ',receivedMsg)
    clientfd.send(bytes(replyMessage,'utf-8'))
    # choice = input('Continue?(y/n)')
    # if(choice=='n'):
        # break
