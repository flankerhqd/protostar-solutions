import socket
import struct
import time 

def solve():
    host = "172.16.121.129"
    port = 2998
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    s.connect((host, port))

    data = s.recv(128)
    wanted = struct.unpack("<I", data)[0]
    print "Received: %d" % (wanted)
     
    s.send(str(wanted))
    time.sleep(2)
    answer =  s.recv(1024)
    print answer
     
    s.close()
        
if __name__=="__main__":        
    solve()
