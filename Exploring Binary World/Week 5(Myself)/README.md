#Week 5

## Explore
- [x] Remote debugging over the gdb
```
gdbserver localhost:2000 sample
in radare
r2 -d gdb://localhost:2000

gdbserver --multi localhost:2000 ( able to attach to any process in the target system)
r2 -d gdb://localhost:2000/<PID> (THIS didn't work)
```
reference: https://www.thegeekstuff.com/2014/04/gdbserver-example/

- [ ] Modulus operation in assembly

## Artik blue's article
- [x] [Reversing x32/x64 with radare2 - 12 (defines, unions and bitmaps)](https://artik.blue/reversing-radare-12)
- [ ] [Reverse engineering x64 binaries with Radare2 - 13 (linux systems programming: theory, syscalls, files and ESIL)](https://artik.blue/reversing-radare-13)

## Ioli crackme
- [ ] Crackme0x9 (last one).

## Extra mile
- Learn little bit about fuzzing
gamozo in twitch streaming fuzz week which has 4 streams gone through one and half.
https://www.twitch.tv/search?term=gamozo%20fuzz%20week
