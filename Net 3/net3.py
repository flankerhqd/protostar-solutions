import socket
import struct
import time 

def solve():
    host = "172.16.121.129"
    port = 2996
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    s.connect((host, port))
    
    # All the strings are sent prefixed with their total length + a NULL terminator
    login_string = ("\x17"  + "\x05net3\x00" + "\x0dawesomesauce\x00" + "\x0apassword\x00")

    login_len = len(login_string) 
    
    s.send(struct.pack(">H", login_len))
    s.send(login_string)

    answer =  s.recv(1024)
    print answer
  
    s.close()
        
if __name__=="__main__":        
    solve()
