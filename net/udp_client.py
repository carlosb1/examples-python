import socket
import sys
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address =('localhost', 10000)
message = 'THis is a messagte, it will be repeated'

try :
        print "sending %s" % message
        sent = sock.sendto(message, server_address)
        print 'waiting to receive'
        data, server = sock.recvfrom(4096)

finally:
        sock.close()
