import socket,sys,exceptions
TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024
Conn=False
print '\n\nClient\n\n'
print 'Please Wait While Socket Is Created And Connection To Server Is Established\n\n''Server Replies Are Indicated By > \n'
try:
        Conn=True
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((TCP_IP, TCP_PORT))
        data = s.recv(BUFFER_SIZE)
        print data
        s.send(raw_input())
except:
        print '\n\nError!!!!\n Re Run The Program in \n'
        print 'Error Type::',sys.exc_info()[0]
        Conn=False
        
if Conn == True:
        try:
            while True:
                data = s.recv(BUFFER_SIZE)
                if data.__eq__(''):
                        print '\nClosing Connection!!! '
                        sys.exit()
                print data
        except exceptions.SystemExit:
                pass
        except :
                print '\n\nError!!!!\n Re Run The Program in\n'
                print 'Error Type::',sys.exc_info()[0]
        finally:
                s.close()
