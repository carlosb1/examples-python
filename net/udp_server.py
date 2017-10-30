import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', 10000)
print 'starting up on the %s and port %s' % server_address

sock.bind(server_address)

while True:
    print '\n waiting to receive message'
    data, address = soc.recvfrom(4096)

    print  'received %s bytes from %s' % (len(data), address)
    print  data

    if data:
        sent = sock.send(data, address)
        print "send %s bytes back to %s ", (send,address)

