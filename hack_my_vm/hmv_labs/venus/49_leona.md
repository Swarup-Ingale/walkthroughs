# Target User
ava  -pass: oCXBeeEeYFX34NU

# Method of Solve
- Login using the ssh credentials
- Perform ls -la to list all the files and cat the mission.txt
- All the Dns records and local data is stored in /etc/bind directory
- So lets go to /etc/bind directory and cat the db.venus.hmv file
- Inspect it thoroughly and get the password
  ```
    leona@venus:~$ cd /etc/bind
    leona@venus:/etc/bind$ ls -la
    total 60
    drwxr-sr-x 2 root bind 4096 Apr  5  2024 .
    drwxr-xr-x 1 root root 4096 Mar  2 08:50 ..
    -rw-r--r-- 1 root root 2403 Feb 12  2024 bind.keys
    -rw-r--r-- 1 root root  255 Feb 12  2024 db.0
    -rw-r--r-- 1 root root  271 Feb 12  2024 db.127
    -rw-r--r-- 1 root root  237 Feb 12  2024 db.255
    -rw-r--r-- 1 root root  353 Feb 12  2024 db.empty
    -rw-r--r-- 1 root root  270 Feb 12  2024 db.local
    -rw-r--r-- 1 root bind  613 Apr  5  2024 db.venus.hmv
    -rw-r--r-- 1 root bind  458 Feb 12  2024 named.conf
    -rw-r--r-- 1 root bind  498 Feb 12  2024 named.conf.default-zones
    -rw-r--r-- 1 root bind  307 Apr  5  2024 named.conf.local
    -rw-r--r-- 1 root bind  219 Apr  5  2024 named.conf.options
    -rw-r----- 1 bind bind  100 Apr  5  2024 rndc.key
    -rw-r--r-- 1 root root 1317 Feb 12  2024 zones.rfc1918
    leona@venus:/etc/bind$ cat db.venus.hmv 
    
    ;
    ; BIND data file for local loopback interface
    ;
        604800
    @       IN      SOA     ns1.venus.hmv. root.venus.hmv. (
                                  2         ; Serial
                             604800         ; Refresh
                              86400         ; Retry
                            2419200         ; Expire
                             604800 )       ; Negative Cache TTL
    
    ;@      IN      NS      localhost.
    ;@      IN      A       127.0.0.1
    ;@      IN      AAAA    ::1
    @       IN      NS      ns1.venus.hmv.
    
    ;IP address of Name Server
    
    ns1     IN      A       127.0.0.1
    ava IN      TXT     oCXBeeEeYFX34NU
  ```
- The Password is **oCXBeeEeYFX34NU**

# Commands Used
- ls -la
- cat
