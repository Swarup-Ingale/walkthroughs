# URL
https://training.olicyber.it/challenges#challenge-256

# Concept
To understand what are shared libraries and how to read and understand them in an ELF file.

# Method of Solve
- Navigate to the challenge URL and read it.
- Download the attachment file.
- use ldd command to look for all the linked libraries.
  ```
    ldd sw-02            
	linux-vdso.so.1 (0x00007fbc2645f000)
	F => not found
	L => not found
	A => not found
	G => not found
	{ => not found
	1 => not found
	d => not found
	8 => not found
	d => not found
	b => not found
	5 => not found
	5 => not found
	9 => not found
	} => not found
	libc.so.6 => /usr/lib/x86_64-linux-gnu/libc.so.6 (0x00007fbc2621f000)
	/lib64/ld-linux-x86-64.so.2 (0x00007fbc26461000)
  ```
- The flag is **FLAG{1d8db559}**
