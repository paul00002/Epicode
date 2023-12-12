import socket

sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

sock.bind(('localhost',44444))

while 1:
     dat,addr=sock.recvfrom(1024)
     print(dat)

