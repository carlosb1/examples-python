from multiprocessing import Process, Pipe

import sys

def read(filename, conn):
    conn.send(open(filename).read())

def words(conn):
    data = conn.recv()
    print('Words',len(data.split()))

if __name__ == "__main__":
    parent, child = Pipe()
    p1 = Process(target=read,args=(sys.argv[1],child))
    p1.start()
    p2 = Process(target=words, args=(parent,))
    p2.start()
    p1.join()
    p2.join()


