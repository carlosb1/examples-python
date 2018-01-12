import socket
import select
import signal
import sys

from communication import send, receive

class ChatServer(object):
    def sighandler(self,signum,frame):
        print('Shutting down server...')
        for o in self.outputs:
            o.close()
        self.server.close()
    def __init__(self, port=3490, backlog=5):
        self.clients = 0
        self.clientmap = {}
        self.outputs = []
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)

        self.server.bind(('',port))
        print('Listening to port',port,'...')
        self.server.listen(backlog)
        signal.signal(signal.SIGINT, self.sighandler)


    def get_name(self, client):
        info = self.clientmap[client]
        host, name = info[0][0], info[1]

        return '@'.join((name,host))

    def serve(self):
            inputs = [self.server,sys.stdin]
            self.outputs = []

            running = 1

            while running:
                try:
                    inputready, outputready, exceptready = select.select(inputs, self.outputs, [])
                except select.error as e:
                    break
                except socket.error as e:
                    break

                for s in inputready:
                    if s == self.server:
                        client, address = self.server.accept()
                        print('chatserver: got connection %d from %s' % (client.fileno(), address))

                        cname = receive(client).split('NAME: ')[1]

                        self.clients = 1
                        send(client, 'CLIENT: '+str(address[0]))
                        inputs.append(client)

                        self.clientmap[client] = (address,cname)
                        msg= str('\n(Connected: New client '+str(self.clients)+' from '+ str(self.get_name(client)))

                        for o in self.outputs:
                            send(o,msg)
                            self.outputs.append(client)

                    elif s == sys.stdin:
                        junk = sys.stdin.readline()
                        running = 0
                    else:
                        try:
                            data = receive(s)
                            if data:
                                msg = '\n#['+self.get_name(s)+']>>'+data
                                for o in self.outputs:
                                    if o!=s:
                                        send(o,msg)
                            else:
                                print('chatserver: %d hung up' % s.fileno())
                                self.clients -=1
                                s.close()
                                inputs.remove(s)
                                self.outputs.remove(s)
                                msg = '\n(Hung up: Client from %s)' %self.get_name(s)
                                for o in self.outputs:
                                    send(o,msg)
                        except socket.error as e:
                            inputs.remove(s)
                            self.outputs.remove(s)
                    self.server.close()

if __name__ == '__main__':
    ChatServer().serve()
