'''
Created on 17-Feb-2013

@author: Sai Gopal
'''
from Query.Process_Query import Rec_Query
from DB.Database import Create_Rand_DB
import socket
import threading
from multiprocessing import Lock
DB=Create_Rand_DB("test",500)

TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 4096
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
print '\nServer Up At IP::'+TCP_IP+' And At Port::'+str(TCP_PORT)

class ServeClients(threading.Thread):
        lock = Lock()
        def __init__(self,con,addr):
            self.addr=addr
            self.conn=con
            threading.Thread.__init__(self)

        def run(self):
            print 'Client:',self.addr
            self.conn.sendto("\n>Enter A Query::",addr)  # echo
            data = conn.recv(BUFFER_SIZE)
            ServeClients.lock.acquire()
            try:
                temp=Rec_Query(data,DB)       
                if type(temp) != 'List':         
                    self.conn.sendto(temp,addr)  # echo
                else:
                    self.conn.sendto("YET TO DO",addr) 
            
                self.conn.close();
            finally:
                ServeClients.lock.release()  

if __name__ == '__main__':
    while True:
        try:
            s.listen(1)
            conn, addr = s.accept()
            print 'Client Connected::', addr
            ServeClients(conn,addr).start()
        except:
            print 'Server Closed!!!!!!'