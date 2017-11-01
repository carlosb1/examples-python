import socket
import sys


#TODO save as configuration file 
PORT = 7
HOST = 'localhost'

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = (HOST, PORT)
print 'starting up on the %s and port %s' % server_address

sock.bind(server_address)


#TODO loop to large files
while True:
    print '\n waiting to receive message'
    data, address = sock.recvfrom(4096)

    print  'received %s bytes from %s' % (len(data), address)
    print  data

    if data:
        sent = sock.sendto(data, address)
        print "send %s bytes back to %s ", (sent,address)

