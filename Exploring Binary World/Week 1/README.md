# Week 1 

## Lessons

### Basic Reversing
- [x] [Intel - x64 assembly Introduction](https://software.intel.com/content/www/us/en/develop/articles/introduction-to-x64-assembly.html)
  - [ ] Take Notes.
- [x] [x64 Reverse Engineering basics](https://nora.codes/tutorial/an-intro-to-x86_64-reverse-engineering/)
  - [ ] Need to work on Crackme3 ( assembly code differs from the blog ). Need to dig into it.
- [x] [Reverse Engineering Tools comparision](https://dustri.org/b/radare2-ida-pro-and-binary-ninja-a-metaphoric-comparison.html)

### Reversing with radare2 (ArtikBlue's article)

- [x] [Reversing x32/x64 with radare2 - 1 (intro) ](https://artik.blue/reversing-radare2-1)
- [x] [Reversing x32/x64 with radare2 - 2 (conditionals) ](https://artik.blue/reversing-radare2-2)
- [x] [Reversing x32/x64 with radare2 - 3 (funcs, cases and loops)](https://artik.blue/reversing-radare-3)
- [x] [Reversing x32/x64 with radare2 - 4 - I ((arrays and strings))](https://artik.blue/reversing-radare-4)

## Pratice Problems
- [x] Re-create the examples on artikBlue's posts
  - [x] Recreate 1 and 2 article binaries and analyze it in radare2
  - [x] Patching binaries (decrese the loop counter) in [Reversing x32/x64 with radare2 - 3 (funcs, cases and loops)](https://artik.blue/reversing-radare-3)
  - [x] r2frida automating reversing in [Reversing x32/x64 with radare2 - 4 - I ((arrays and strings))](https://artik.blue/reversing-radare-4)
  Instead of r2frida i used r2pipe to automate this.
- [x] Ioli crackme 1

## Extra mile
- Install radare2 on a Windows BOX 
  - Re-create some of the examples shown in the posts 
  - Try to break the IOLI crackme 0x00 (.exe) in Windows using r2
- Use GHIDRA instead of radare2 
  - [Video on using Ghidra for Reversing crackMe](https://www.youtube.com/watch?v=6p5Qviusskk)

## Questions
- Double value in the memory is different from float value, ArtikBlue article 2.

## CheatSheet
- [Radare 2 cheatsheet](https://github.com/radareorg/radare2/blob/master/doc/intro.md)
