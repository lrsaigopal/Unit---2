
from Query.Process_Query import Rec_Query
from DB.Database import Create_Rand_DB
import socket
import threading
from multiprocessing import Lock
import datetime
import os
import types

DB=Create_Rand_DB("test.txt",500)

TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 4096
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.bind((TCP_IP, TCP_PORT))
except:
    print 'Port Already In Use!!!!!!Exiting'
    exit(1)
now = datetime.datetime.now()
print '\nServer Up At IP::'+TCP_IP+' And At Port::'+str(TCP_PORT)+' At '+str(now)+' \n Check Log File For Info'
logfil='Log@'+str(now)+'.txt'
logfil=logfil.replace(':', '-');

f =open(logfil,'w',0)

f.write('\nServer Up At IP::'+TCP_IP+' And At Port::'+str(TCP_PORT)+' At '+str(now)+'\n')

class ServeClients(threading.Thread):
        lock = Lock()
        def __init__(self,con,addr):
            self.addr=addr
            self.conn=con
            threading.Thread.__init__(self)

        def run(self):
            self.conn.sendto("\n>Enter A Query::",addr)  # echo
            data = conn.recv(BUFFER_SIZE)
            now = datetime.datetime.now()
            f.write("Query Recived From "+str(addr)+" @ "+str(now)+'::'+data+'\n')
            ServeClients.lock.acquire()
            try:
                temp=Rec_Query(data,DB)
                self.conn.sendto('\n\n',addr)         
       
                if type(temp)==types.ListType:
                    for i in temp:
                        self.conn.sendto(i,addr)
                    self.conn.sendto('\n\nEnd Of Results',addr)         
                else:
                    self.conn.sendto(temp,addr)  # echo                     
                self.conn.close();
            finally:
                ServeClients.lock.release()  

if __name__ == '__main__':
    while True:
        try:
            s.listen(1)
            conn, addr = s.accept()
            f.write('Client Connected::'+str(addr)+'\n')
            ServeClients(conn,addr).start()
        except:
            now = datetime.datetime.now()
            f.write('Server Shutoff @'+str(now)+'\n')
            print 'Server Shutoff@'+str(now)
            f.close()
            exit(0)
            