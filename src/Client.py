import socket,sys
TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024
print '\n\nClient\n\n'
print 'Please Wait While Socket Is Created And Connection To Server Is Established\n\n''Server Replies Are Indicated By > \n'
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    data = s.recv(BUFFER_SIZE)
    print data
    s.send(raw_input())
    data = s.recv(BUFFER_SIZE)
    s.close()
    print data
except :
    print '\n\nError!!!!\n Re Run The Program\n'
    print 'Error Type::',sys.exc_info()[0]
