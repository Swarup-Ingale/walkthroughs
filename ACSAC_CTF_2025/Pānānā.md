# Pānānā — Walkthrough

**Category:** sanity-check  
**Difficulty:** tutorial  
**Author:** mahaloz

## Overview

This is a **sanity check** challenge designed to help you get familiar with the CTF infrastructure. Your goal is to retrieve the flag from `/flag` by running the provided binary.

## Steps

### 1. SSH into the Challenge Server

The challenge provides SSH credentials, connect and start the challenge.

### 2. Explore the Challenge Directory

Once connected, list the contents of `/challenge/`:

```bash
ls /challenge/
```

You should see:

- `README.md` — challenge description
- `source.c` — the source code of the binary
- `run` — the compiled challenge binary

### 3. Understand the Source Code

Read `/challenge/source.c` to understand what the binary does:

```c
#include <stdio.h>
#include <unistd.h>
#include <fcntl.h>

int main() {
    printf("\n\n===========================================\n");
    printf("         Welcome to the ACSAC CTF!\n");
    printf("===========================================\n\n\n");
    int fd = open("/flag", 0);
    char buf[100];
    buf[read(fd, buf, 100)] = 0;
    printf("Here is the flag: %s\n", buf);
    return 0;
}
```

The program simply opens `/flag`, reads its contents into a buffer, and prints it out. The binary is **setuid** (or has appropriate permissions) to allow reading `/flag`, which is otherwise inaccessible to your user.

### 4. Run the Binary

Execute the challenge binary:

```bash
/challenge/run
```

You will see the ACSAC CTF banner printed, followed by the flag.

### 5. Submit the Flag

Copy the flag from the output and submit it to the CTF platform.

## Key Takeaways

- All challenge files are located in `/challenge/`.
- Challenge binaries are designed to be run with `/challenge/run`.
- The `/flag` file is not directly readable — you must use the provided binary.
- `sudo` is available in practice mode for debugging with root privileges.
