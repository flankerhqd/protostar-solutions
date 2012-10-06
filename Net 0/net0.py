import socket
import struct

def solve():
    host = "172.16.121.129"
    port = 2999
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    s.connect((host, port))
    
    data = s.recv(128)
    print "Received: %s" % (data)
    
    wanted = int(data.split()[2].split('\'')[1])
    print "Random num: %d" % (wanted)
    
    s.send(struct.pack("<I", wanted))
    answer =  s.recv(1024)
    print answer

    s.close()
        
if __name__=="__main__":        
    solve()
