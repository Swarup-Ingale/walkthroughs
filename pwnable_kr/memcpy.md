# URL
https://pwnable.kr/play.php

# SSH Credentials
ssh memcpy@pwnable.kr -p2222 (pw:guest)

**Challenge:** memcpy  
**Category:** Binary Exploitation / Memory Alignment  
**Goal:** Provide the correct malloc sizes so the SSE-based `fast_memcpy` does not crash on misaligned memory, allowing all 10 experiments to complete and reveal the flag.

---

## Challenge Overview

The challenge server runs a 32-bit ELF binary (`memcpy`) that benchmarks two memcpy implementations:
- `slow_memcpy` — byte-by-byte copy
- `fast_memcpy` — 64-byte block copy using SSE instructions (`movdqa`, `movntps`)

The program asks for 10 sizes (one per experiment, each in a specified power-of-2 range). It then allocates a buffer of that size with `malloc`, runs `slow_memcpy` and `fast_memcpy`, and prints cycle counts. After all 10 experiments succeed, the flag is printed.

The catch: `fast_memcpy` uses **`movdqa`** (aligned load) and **`movntps`** (aligned nontemporal store), which require 16-byte aligned source **and** destination addresses. On a 32-bit system, `malloc` only guarantees 8-byte alignment, so the destination pointer is often misaligned — causing a segfault when `fast_memcpy` runs with size >= 64.

---

## Provided Files

### Source Code (`memcpy.c`)

```c
// gcc -o memcpy memcpy.c -m32 -lm
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <signal.h>
#include <unistd.h>
#include <sys/mman.h>
#include <math.h>

unsigned long long rdtsc(){
    asm("rdtsc");
}

char* slow_memcpy(char* dest, const char* src, size_t len){
    int i;
    for (i=0; i<len; i++) {
        dest[i] = src[i];
    }
    return dest;
}

char* fast_memcpy(char* dest, const char* src, size_t len){
    size_t i;
    if(len >= 64){
        i = len / 64;
        len &= (64-1);
        while(i-- > 0){
            __asm__ __volatile__ (
            "movdqa (%0), %%xmm0\n"
            "movdqa 16(%0), %%xmm1\n"
            "movdqa 32(%0), %%xmm2\n"
            "movdqa 48(%0), %%xmm3\n"
            "movntps %%xmm0, (%1)\n"
            "movntps %%xmm1, 16(%1)\n"
            "movntps %%xmm2, 32(%1)\n"
            "movntps %%xmm3, 48(%1)\n"
            ::"r"(src),"r"(dest):"memory");
            dest += 64;
            src += 64;
        }
    }
    if(len) slow_memcpy(dest, src, len);
    return dest;
}

int main(void){
    setvbuf(stdout, 0, _IONBF, 0);
    setvbuf(stdin, 0, _IOLBF, 0);

    printf("Hey, I have a boring assignment for CS class.. :(\n");
    printf("The assignment is simple.\n");
    printf("-----------------------------------------------------\n");
    printf("- What is the best implementation of memcpy?        -\n");
    printf("- 1. implement your own slow/fast version of memcpy -\n");
    printf("- 2. compare them with various size of data         -\n");
    printf("- 3. conclude your experiment and submit report     -\n");
    printf("-----------------------------------------------------\n");
    printf("This time, just help me out with my experiment and get flag\n");
    printf("No fancy hacking, I promise :D\n");

    unsigned long long t1, t2;
    int e;
    char* src;
    char* dest;
    unsigned int low, high;
    unsigned int size;
    char* cache1 = mmap(0, 0x4000, 7, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0);
    char* cache2 = mmap(0, 0x4000, 7, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0);
    src = mmap(0, 0x2000, 7, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0);

    size_t sizes[10];
    int i=0;

    for(e=4; e<14; e++){
        low = pow(2,e-1);
        high = pow(2,e);
        printf("specify the memcpy amount between %d ~ %d : ", low, high);
        scanf("%d", &size);
        if( size < low || size > high ){
            printf("don't mess with the experiment.\n");
            exit(0);
        }
        sizes[i++] = size;
    }

    sleep(1);
    printf("ok, lets run the experiment with your configuration\n");
    sleep(1);

    for(i=0; i<10; i++){
        size = sizes[i];
        printf("experiment %d : memcpy with buffer size %d\n", i+1, size);
        dest = malloc( size );

        memcpy(cache1, cache2, 0x4000);
        t1 = rdtsc();
        slow_memcpy(dest, src, size);
        t2 = rdtsc();
        printf("ellapsed CPU cycles for slow_memcpy : %llu\n", t2-t1);

        memcpy(cache1, cache2, 0x4000);
        t1 = rdtsc();
        fast_memcpy(dest, src, size);
        t2 = rdtsc();
        printf("ellapsed CPU cycles for fast_memcpy : %llu\n", t2-t1);
        printf("\n");
    }

    printf("thanks for helping my experiment!\n");
    printf("flag : [erased here. get it from server]\n");
    return 0;
}
```

### Dockerfile

```dockerfile
FROM ubuntu:16.04

RUN dpkg --add-architecture i386 && \
    apt update && \
    apt install -y gcc-multilib libc6:i386 lib32stdc++6 lib32z1 gdb file net-tools

RUN apt-get install -y perl
RUN useradd -u 1089 -m memcpy_pwn

COPY memcpy.c /home/memcpy_pwn/memcpy.c
COPY super.pl /home/memcpy_pwn/super.pl

RUN chown root:memcpy_pwn /home/memcpy_pwn/memcpy.c /home/memcpy_pwn/super.pl
WORKDIR /home/memcpy_pwn
RUN gcc -o memcpy memcpy.c -m32 -lm
RUN chown root:memcpy_pwn /home/memcpy_pwn/memcpy
RUN chmod 550 /home/memcpy_pwn/memcpy
RUN chmod 550 /home/memcpy_pwn/super.pl

USER memcpy_pwn
WORKDIR /home
CMD ["perl", "/home/memcpy_pwn/super.pl"]
```

### `super.pl` (network daemon)

```perl
#!/usr/bin/perl
use Socket;
$port = 9022;
@exec = ("/home/memcpy_pwn/memcpy");
socket(SERVER, PF_INET, SOCK_STREAM, 6);
setsockopt(SERVER, SOL_SOCKET, SO_REUSEADDR, pack("l", 1));
bind(SERVER, sockaddr_in($port, INADDR_ANY));
listen(SERVER,SOMAXCONN);
$SIG{"CHLD"} = "IGNORE";
while($addr = accept CLIENT, SERVER){
    $| = 1;
    ($port, $packed_ip) = sockaddr_in($addr);
    $datestring = localtime();
    $ip = inet_ntoa($packed_ip);
    print "$ip: $port connected($datestring)\n";
    fork || do {
        $| = 1;
        close SERVER;
        open STDIN,  "<&CLIENT";
        open STDOUT, ">&CLIENT";
        open STDERR, ">&CLIENT";
        close CLIENT;
        exec @exec;
        exit 0;
    };
    close CLIENT;
}
close SERVER;
```

---

## Vulnerability Analysis

### The SSE Alignment Requirement

The `fast_memcpy` function uses these SSE instructions:

```
movdqa  (%0), %%xmm0    ; load 16 bytes from src  — needs 16-byte alignment
movntps %%xmm0, (%1)    ; store 16 bytes to dest — needs 16-byte alignment
```

- `movdqa` (Move Double Quadword Aligned): raises #GP (general protection fault) if the memory operand is not 16-byte aligned.
- `movntps` (Move Non-Temporal Packed Single): also requires 16-byte alignment.

### Why It Crashes

The binary is compiled with `-m32` (32-bit). On x86-32 glibc:
- `MALLOC_ALIGNMENT` = `2 * SIZE_SZ` = **8 bytes**
- `malloc` returns pointers aligned to **8 bytes**, not 16.

Meanwhile, `src` is allocated via `mmap` (page-aligned → 4096-byte aligned), so it is always fine.

`dest = malloc(size)` returns an 8-byte aligned address. When `fast_memcpy` attempts `movntps` to this address, it segfaults if the address is not a multiple of 16.

### When Does It Crash?

`fast_memcpy` only runs the SSE path when `len >= 64`. For sizes below 64, it falls through to `slow_memcpy`, so no crash.

The experiment ranges are:

| Exp | e   | low     | high    | notes                 |
|-----|-----|---------|---------|-----------------------|
| 1   | 4   | 8       | 16      | all < 64, safe        |
| 2   | 5   | 16      | 32      | all < 64, safe        |
| 3   | 6   | 32      | 64      | safe if < 64          |
| 4   | 7   | 64      | 128     | **needs alignment**   |
| 5   | 8   | 128     | 256     | **needs alignment**   |
| 6   | 9   | 256     | 512     | **needs alignment**   |
| 7   | 10  | 512     | 1024    | **needs alignment**   |
| 8   | 11  | 1024    | 2048    | **needs alignment**   |
| 9   | 12  | 2048    | 4096    | **needs alignment**   |
| 10  | 13  | 4096    | 8192    | **needs alignment**   |

Experiments 4–10 always have size >= 64, so their `dest` must be 16-byte aligned.

---

## Exploit Strategy: Controlling Heap Alignment

Since `malloc` allocations are contiguous on the heap (no frees happen between experiments), the address returned by `malloc` depends on the **sum of all previous chunk sizes**.

### glibc Chunk Size Calculation

On 32-bit glibc (Ubuntu 16.04, glibc 2.23):

```
chunk_size = request2size(req)
           = max( MINSIZE, (req + SIZE_SZ + MALLOC_ALIGN_MASK) & ~MALLOC_ALIGN_MASK )
```

Where:
- `SIZE_SZ` = 4
- `MALLOC_ALIGN_MASK` = 7
- `MINSIZE` = 24 bytes (minimum chunk to hold free-list pointers)

So:
```
chunk_size = max( 24, (req + 4 + 7) & ~7 )
           = max( 24, (req + 11) / 8 * 8 )   # integer division
```

The returned data pointer is at `chunk_address + 8` (after the 8-byte header).

### Alignment Condition

Let the heap base be at address `A` (page-aligned, so `A ≡ 0 mod 16`). For experiment `k` (0-indexed), the `dest` pointer is:

```
dest_k = A + Σ(chunk_size_0 .. chunk_size_{k-1}) + 8
```

For `dest_k` to be 16-byte aligned:

```
Σ(chunk_size_0 .. chunk_size_{k-1}) + 8 ≡ 0 mod 16
Σ(chunk_size_0 .. chunk_size_{k-1}) ≡ 8 mod 16
```

The initial alignment is always off by 8 (since data starts at `A + 8`), so experiments 1–3 avoid the SSE path by using sizes < 64. For experiment 4 onward, we choose the **previous** experiment's size so the cumulative sum is `≡ 8 mod 16`.

## Solution

After iterative calculation (or trial-and-error with GDB in the Docker container), the following sizes produce 16-byte aligned `dest` pointers for every experiment that needs it:

```python
solution = [8, 16, 32, 72, 135, 263, 519, 1031, 2055, 4096]
```

### Verification

Connect to the challenge server and provide these values:

```bash
$ nc pwnable.kr 9022
```

Full interactive session:

```
specify the memcpy amount between 8 ~ 16 : 8
specify the memcpy amount between 16 ~ 32 : 16
specify the memcpy amount between 32 ~ 64 : 32
specify the memcpy amount between 64 ~ 128 : 72
specify the memcpy amount between 128 ~ 256 : 135
specify the memcpy amount between 256 ~ 512 : 263
specify the memcpy amount between 512 ~ 1024 : 519
specify the memcpy amount between 1024 ~ 2048 : 1031
specify the memcpy amount between 2048 ~ 4096 : 2055
specify the memcpy amount between 4096 ~ 8192 : 4096
```

### Expected Output

```
ok, lets run the experiment with your configuration
experiment 1 : memcpy with buffer size 8
ellapsed CPU cycles for slow_memcpy : 1930
ellapsed CPU cycles for fast_memcpy : 196

experiment 2 : memcpy with buffer size 16
ellapsed CPU cycles for slow_memcpy : 250
ellapsed CPU cycles for fast_memcpy : 178

experiment 3 : memcpy with buffer size 32
ellapsed CPU cycles for slow_memcpy : 452
ellapsed CPU cycles for fast_memcpy : 512

experiment 4 : memcpy with buffer size 72
ellapsed CPU cycles for slow_memcpy : 928
ellapsed CPU cycles for fast_memcpy : 238

experiment 5 : memcpy with buffer size 135
ellapsed CPU cycles for slow_memcpy : 1722
ellapsed CPU cycles for fast_memcpy : 224

experiment 6 : memcpy with buffer size 263
ellapsed CPU cycles for slow_memcpy : 3212
ellapsed CPU cycles for fast_memcpy : 280

experiment 7 : memcpy with buffer size 519
ellapsed CPU cycles for slow_memcpy : 6268
ellapsed CPU cycles for fast_memcpy : 318

experiment 8 : memcpy with buffer size 1031
ellapsed CPU cycles for slow_memcpy : 12258
ellapsed CPU cycles for fast_memcpy : 402

experiment 9 : memcpy with buffer size 2055
ellapsed CPU cycles for slow_memcpy : 24354
ellapsed CPU cycles for fast_memcpy : 572

experiment 10 : memcpy with buffer size 4096
ellapsed CPU cycles for slow_memcpy : 48404
ellapsed CPU cycles for fast_memcpy : 972

thanks for helping my experiment!
flag : b0thers0m3_m3m0ry_4lignment
```

---

## Flag

```
b0thers0m3_m3m0ry_4lignment
```
- So the Final Flag is **b0thers0m3_m3m0ry_4lignment**

---

## One-Liner

```bash
printf "8\n16\n32\n72\n135\n263\n519\n1031\n2055\n4096\n" | nc pwnable.kr 9022
```

---

## Root Cause & Mitigation

### Root Cause

The 32-bit binary uses SSE instructions (`movdqa`, `movntps`) that require 16-byte alignment, but `malloc` on 32-bit glibc only guarantees 8-byte alignment. The `dest` pointer from `malloc` is misaligned, causing a segfault in `fast_memcpy` when `size >= 64`.

### Mitigation

1. Use **`movdqu`** (Move Double Quadword **Unaligned**) and **`movups`**/**`movntps`** instead of `movdqa`/`movntps` — these tolerate misaligned addresses (at a minor performance cost).
2. Align the `dest` pointer explicitly: round up the `malloc` return value to the next 16-byte boundary before passing it to `fast_memcpy`.
3. Use `posix_memalign` to request 16-byte aligned memory.

---

## Key Takeaways

| Concept | Detail |
|---------|--------|
| **Challenge Type** | Memory Alignment / SSE Requirements |
| **Vulnerability** | `movdqa`/`movntps` on potentially misaligned heap pointers |
| **Exploit Technique** | Heap address manipulation via controlled malloc sizes |
| **Impact** | Program crash; bypassed to retrieve flag |
| **Fix** | Use unaligned SSE instructions or explicit alignment |
