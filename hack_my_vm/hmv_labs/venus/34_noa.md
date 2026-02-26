# Target User
maia  -pass: nh1hnDPHpydEjoEN

# Method of Solve
- Login using the ssh credentials
- Perform ls -la to list all the files in the directory and cat the mission.txt
- use xxd to see the raw output and look for a suspicious string in the output
  ```
    noa@venus:~$ xxd trash
    000006f0: cd6b 91a0 156c 66c8 dfe1 d107 74f3 4857  .k...lf.....t.HW
    00000700: 4e1b b71c 84df 6ff5 b195 6808 c196 33e8  N.....o...h...3.
    00000710: e2bd 1edc 32ec 5593 a439 ea53 c4e9 08aa  ....2.U..9.S....
    00000720: e1d7 1f94 2c4f bd4a 4081 7774 05c3 daa6  ....,O.J@.wt....
    00000730: 05eb 0a99 1f0b 568f 673b f8de 3e10 b811  ......V.g;..>...
    00000740: 78d4 d6bd e23a b0f4 a391 c5f3 50c1 be4b  x....:......P..K
    00000750: 32d7 6994 c89a 5353 a3aa bf7b fd78 6646  2.i...SS...{.xfF
    00000760: 4ebf 81f6 d8d6 b1f4 937b a99c 5c6e 6831  N........{..\nh1
    00000770: 686e 4450 4870 7964 456a 6f45 4e0a 6735  hnDPHpydEjoEN.g5
    00000780: 31f8 5ba5 b311 7c3e 99c2 2770 d792 8059  1.[...|>..'p...Y
    00000790: 50c4 d65c 8fb2 89cc 74d3 1863 a60b be1c  P..\....t..c....
    000007a0: 8fdc d6b2 e221 7c01 4ce7 092f c5a4 2c2e  .....!|.L../..,.
    000007b0: 48c1 d545 39f4 e41d 8799 92b4 f5db 6123  H..E9.........a#
  ```
- Or use strings command
  ```
    noa@venus:~$ strings -14 trash 
    \nh1hnDPHpydEjoEN
  ```
- We ge the password which is **nh1hnDPHpydEjoEN**

# Commands Used
- ls -la
- cat
- xxd
- strings
