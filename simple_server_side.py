#Simple Server Side

import socket

s = socket.socket()
host = socket.gethostname()  #gets the current machine name
port = 9999

s.bind((host,port))  

print("Waiting for connection....")
s.listen(5)

while True:
    conn,addr = s.accept()  #connects and accept fromm client
    print("Got connection from ",addr)
    conn.send()
    conn.close()   #closes the connection
