# URL
https://training.olicyber.it/challenges#challenge-257

# Concept
To understand the sections present in an elf file and how we can read them from x86_64 to plain text or understand them.

# Method of Solve
- Navigate to the challenge URL and read the description.
- Download the challenge binary file in attachment.
- use objdump -h flag to list all the important sections in the elf.
  ```
    objdump -h sw-03

      sw-03:     file format elf64-x86-64
      
      Sections:
      Idx Name          Size      VMA               LMA               File off  Algn
        0 .interp       0000001c  00000000000002a8  00000000000002a8  000002a8  2**0
                        CONTENTS, ALLOC, LOAD, READONLY, DATA
        1 .note.gnu.build-id 00000024  00000000000002c4  00000000000002c4  000002c4  2**2
                        CONTENTS, ALLOC, LOAD, READONLY, DATA
        2 .note.ABI-tag 00000020  00000000000002e8  00000000000002e8  000002e8  2**2
                        CONTENTS, ALLOC, LOAD, READONLY, DATA
        3 .gnu.hash     00000024  0000000000000308  0000000000000308  00000308  2**3
                        CONTENTS, ALLOC, LOAD, READONLY, DATA
        4 .dynsym       00000090  0000000000000330  0000000000000330  00000330  2**3
                        CONTENTS, ALLOC, LOAD, READONLY, DATA
        5 .dynstr       0000007d  00000000000003c0  00000000000003c0  000003c0  2**0
                        CONTENTS, ALLOC, LOAD, READONLY, DATA
        6 .gnu.version  0000000c  000000000000043e  000000000000043e  0000043e  2**1
                        CONTENTS, ALLOC, LOAD, READONLY, DATA
        7 .gnu.version_r 00000020  0000000000000450  0000000000000450  00000450  2**3
                        CONTENTS, ALLOC, LOAD, READONLY, DATA
        8 .rela.dyn     000000c0  0000000000000470  0000000000000470  00000470  2**3
                        CONTENTS, ALLOC, LOAD, READONLY, DATA
        9 .init         00000017  0000000000001000  0000000000001000  00001000  2**2
                        CONTENTS, ALLOC, LOAD, READONLY, CODE
       10 .plt          00000010  0000000000001020  0000000000001020  00001020  2**4
                        CONTENTS, ALLOC, LOAD, READONLY, CODE
       11 .plt.got      00000008  0000000000001030  0000000000001030  00001030  2**3
                        CONTENTS, ALLOC, LOAD, READONLY, CODE
       12 .text         00000151  0000000000001040  0000000000001040  00001040  2**4
                        CONTENTS, ALLOC, LOAD, READONLY, CODE
       13 .fini         00000009  0000000000001194  0000000000001194  00001194  2**2
                        CONTENTS, ALLOC, LOAD, READONLY, CODE
       14 .rodata       00000004  0000000000002000  0000000000002000  00002000  2**2
                        CONTENTS, ALLOC, LOAD, READONLY, DATA
       15 .eh_frame_hdr 0000003c  0000000000002004  0000000000002004  00002004  2**2
                        CONTENTS, ALLOC, LOAD, READONLY, DATA
       16 .eh_frame     00000108  0000000000002040  0000000000002040  00002040  2**3
                        CONTENTS, ALLOC, LOAD, READONLY, DATA
       17 .init_array   00000008  0000000000003e18  0000000000003e18  00002e18  2**3
                        CONTENTS, ALLOC, LOAD, DATA
       18 .fini_array   00000008  0000000000003e20  0000000000003e20  00002e20  2**3
                        CONTENTS, ALLOC, LOAD, DATA
       19 .dynamic      000001b0  0000000000003e28  0000000000003e28  00002e28  2**3
                        CONTENTS, ALLOC, LOAD, DATA
       20 .got          00000028  0000000000003fd8  0000000000003fd8  00002fd8  2**3
                        CONTENTS, ALLOC, LOAD, DATA
       21 .got.plt      00000018  0000000000004000  0000000000004000  00003000  2**3
                        CONTENTS, ALLOC, LOAD, DATA
       22 .data         00000010  0000000000004018  0000000000004018  00003018  2**3
                        CONTENTS, ALLOC, LOAD, DATA
       23 .bss          00000008  0000000000004028  0000000000004028  00003028  2**0
                        ALLOC
       24 .comment      0000001b  0000000000000000  0000000000000000  00003028  2**0
                        CONTENTS, READONLY
       25 .super-secret-section 0000001c  0000000000000000  0000000000000000  00003043  2**0
                        CONTENTS, READONLY
       26 .debug_aranges 000000f0  0000000000000000  0000000000000000  00003060  2**4
                        CONTENTS, READONLY, DEBUGGING, OCTETS
       27 .debug_info   00000583  0000000000000000  0000000000000000  00003150  2**0
                        CONTENTS, READONLY, DEBUGGING, OCTETS
       28 .debug_abbrev 00000177  0000000000000000  0000000000000000  000036d3  2**0
                        CONTENTS, READONLY, DEBUGGING, OCTETS
       29 .debug_line   0000021a  0000000000000000  0000000000000000  0000384a  2**0
                        CONTENTS, READONLY, DEBUGGING, OCTETS
       30 .debug_str    000003b9  0000000000000000  0000000000000000  00003a64  2**0
                        CONTENTS, READONLY, DEBUGGING, OCTETS
       31 .debug_ranges 00000080  0000000000000000  0000000000000000  00003e20  2**4
                        CONTENTS, READONLY, DEBUGGING, OCTETS
  ```
- The most interesting and juicy section looks like the **.super-secret-section** so lets analyze it further.
- For this we will use -s -j flags of the objdump.
  ```
    objdump -s -j .super-secret-section sw-03
      
      sw-03:     file format elf64-x86-64
      
      Contents of section .super-secret-section:
       0000 46004c00 41004700 7b006400 30003300  F.L.A.G.{.d.0.3.
       0010 6c007600 6e003400 69007d00           l.v.n.4.i.}.
  ```
- The flag is **flag{d03lvn4i}**
