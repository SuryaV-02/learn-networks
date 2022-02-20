import socket,sys,time

start_time = time.time()
clientFd = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
clientFd.connect(('localhost',55555))

message = 'Trying to estimate the RTT.. please wait'
clientFd.sendto(bytes(message,'utf-8'),('localhost',55555))
reply,address = clientFd.recvfrom(1024)
print(address,' replayied with ',reply)
end_time = time.time()

print('RTT = {}'.format(end_time-start_time))