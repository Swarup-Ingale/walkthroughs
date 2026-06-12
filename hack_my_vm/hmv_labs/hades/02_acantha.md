# Target User
alala -password : DsYzpJQrCEndEWIMxWxu

# Method of Solve
- connect to the ssh environment and perform ls -la to list all the files in the directory
- cat the mission.txt to understand the approach and motive of challenge.
- A guess file is given which is elf executable binary.
- Apply strings command and get the password.
  ```
    acantha@hades:~$ strings guess 
    je?}
    /lib64/ld-linux-x86-64.so.2
    puts
    __libc_start_main
    __cxa_finalize
    printf
    __isoc99_scanf
    libc.so.6
    GLIBC_2.7
    GLIBC_2.2.5
    GLIBC_2.34
    _ITM_deregisterTMCloneTable
    __gmon_start__
    _ITM_registerTMCloneTable
    PTE1
    u+UH
    Enter PIN code:
    DsYzpJQrCEndEWIMxWxu
    NO :_(
    ;*3$"
    GCC: (Debian 14.2.0-19) 14.2.0
  ```
- The Password is **DsYzpJQrCEndEWIMxWxu**

# Commands Used
- strings
- ls
- cat
