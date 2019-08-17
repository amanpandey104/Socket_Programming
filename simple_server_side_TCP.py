#Simple Server Side

import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = socket.gethostname()  #gets the current machine name
port = 9999

s.bind((host,port))  

print("Waiting for connection....")
s.listen(5)

while True:
    conn,addr = s.accept()  #connects and accept fromm client
    print("Got connection from ",addr)
    msg = b''
    conn.send(msg)
    conn.close()   #closes the connection
