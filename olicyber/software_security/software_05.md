# URL
https://training.olicyber.it/challenges#challenge-259

# Concept
To Understand how elf files are read in ghidra and how can we reverse them to obtain information hidden in them.

# Method of Solve
- Navigate to the challenge URL and read the description.
- Download the elf binary file in attachment.
- open it in ghidra and read it after reversing
- then perform objdump -d -M intel to set the dissassembly favour to intel and get its object dump.
  ```
    objdump -d -M intel sw-05                

      sw-05:     file format elf64-x86-64
      
      
      Disassembly of section .init:
      
      0000000000001000 <_init>:
          1000:	48 83 ec 08          	sub    rsp,0x8
          1004:	48 8b 05 dd 2f 00 00 	mov    rax,QWORD PTR [rip+0x2fdd]        # 3fe8 <__gmon_start__>
          100b:	48 85 c0             	test   rax,rax
          100e:	74 02                	je     1012 <_init+0x12>
          1010:	ff d0                	call   rax
          1012:	48 83 c4 08          	add    rsp,0x8
          1016:	c3                   	ret
      
      Disassembly of section .plt:
      
      0000000000001020 <.plt>:
          1020:	ff 35 e2 2f 00 00    	push   QWORD PTR [rip+0x2fe2]        # 4008 <_GLOBAL_OFFSET_TABLE_+0x8>
          1026:	ff 25 e4 2f 00 00    	jmp    QWORD PTR [rip+0x2fe4]        # 4010 <_GLOBAL_OFFSET_TABLE_+0x10>
          102c:	0f 1f 40 00          	nop    DWORD PTR [rax+0x0]
      
      0000000000001030 <puts@plt>:
          1030:	ff 25 e2 2f 00 00    	jmp    QWORD PTR [rip+0x2fe2]        # 4018 <puts@GLIBC_2.2.5>
          1036:	68 00 00 00 00       	push   0x0
          103b:	e9 e0 ff ff ff       	jmp    1020 <.plt>
  .
  .
  .
  .
  ```
  - After reading everything we notice that the elf file checks for strings comparisons at multiple indexes of memory and then finally prints correct message.
  - So now we will read the readonly data of the file, and first read only top 20 lines to avoid complexities
    ```
    objdump -s -j .rodata sw-05              

    sw-05:     file format elf64-x86-64
    
    Contents of section .rodata:
     2000 01000200 00000000 00000000 00000000  ................
     2010 66006c00 61006700 7b003800 31003700  f.l.a.g.{.8.1.7.
     2020 35003000 65003600 33007d00 f09f9aa9  5.0.e.6.3.}.....
     2030 20517561 6c20c3a8 206c6120 666c6167   Qual .. la flag
     2040 3f203a20 00e29d8c 20536261 676c6961  ? : .... Sbaglia
     2050 746f2120 50726f76 6120616e 636f7261  to! Prova ancora
     2060 00e29c85 20476975 73746f21 00        .... Giusto!.
    ```
  - As we can see the flag is visible.
  - The flag is **flag{81750e63}**
