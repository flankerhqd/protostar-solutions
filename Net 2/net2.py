import socket
import struct
import time 

def solve():
    host = "172.16.121.129"
    port = 2997
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    s.connect((host, port))

    wanted_sum = 0
    for i in range (0, 4):
        data = s.recv(4)
        n = struct.unpack("<I", data)[0]
        print "Received: %d" % (n)
        wanted_sum += n

    wanted_sum &= 0xffffffff
    print "Wanted sum: %d" % (wanted_sum)
    
    s.send(struct.pack("<I", wanted_sum))
 
    answer = s.recv(1024)
    print answer
     
    s.close()
        
if __name__=="__main__":        
    solve()
