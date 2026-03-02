# Target User
adela  -pass: nbhlQyKuaXGojHx

# Method of Solve
- Login using the ssh credentials
- Perform ls -la to list all the files and cat the mission.txt
- make a tmp folder in tmp directory named adela and copy all the files (id_rsa.pub, id_rsa.pem, pass.enc) to the adela folder
- Now use openssl and pkeyutl to decrypt the pass.enc using the id_rsa.pem and store it in password.txt
- cat the password.txt to get the password
  ```
    irene@venus:/tmp/adela$ openssl pkeyutl -decrypt -inkey id_rsa.pem -in pass.enc -out password.txt
    irene@venus:/tmp/adela$ cat password.txt
    nbhlQyKuaXGojHx
  ```
- The Password is **nbhlQyKuaXGojHx**

# Commands Used
- ls -la
- cat
- openssl
- cp
