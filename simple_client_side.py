#simple client side

import socket

s = socket.socket()
host = socket.gethostname()
port = 9999

s.connect((host,port))
print(s.recv(1024))  #1024 is bufsize or max amount

s.close()