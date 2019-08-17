#UDP server side

import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

udp_host = socket.gethostname()
udp_port = 12345

print(type(sock))  #this will show the type of socket

sock.bind((udp_host,udp_port))

while True:
    print("Waiting for the client")
    data,addr = sock.recvfrom(1024)
    print("Received msg from",data,"from",addr)
