import socket
import sys
PORT = 7
HOST = 'localhost'
server_address =(HOST, PORT )

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#TODO add message from command line
message = 'THis is a messagte, it will be repeated'

try :
        print "sending %s" % message
        sent = sock.sendto(message, server_address)
        print 'waiting to receive'
        data, server = sock.recvfrom(4096)
        print "I received: %s bytes with message:  %s" %(len(data), data)
finally:
        sock.close()
