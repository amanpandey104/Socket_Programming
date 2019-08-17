#UDP client side

import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

udp_host = socket.gethostname()
udp_port = 12345

while True:
    msg = b"Socket complete"
    sock.sendto(msg,(udp_host,udp_port))

    
