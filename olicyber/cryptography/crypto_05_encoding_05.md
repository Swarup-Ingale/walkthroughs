# URL
https://training.olicyber.it/challenges#challenge-330

# Concept
To Learn to use bruteforcing to crack a cryptographic password and get the plaintext using xor

# Method of Solve
- Go to the challenge URL and copy the ciphertext
- Write a Python Script to check every possible combination for the xor key to be xored with the ciphertext and get the correct plaintext
  ```
    ciphertext_hex = "104e137f425954137f74107f525511457f5468134d7f146c4c"
    
    # Convert hex to bytes
    cipher_bytes = bytes.fromhex(ciphertext_hex)
    
    def is_printable(text):
        return all(32 <= b <= 126 for b in text)
    
    for key in range(256):
        decrypted = bytes(b ^ key for b in cipher_bytes)
        
        if is_printable(decrypted):
            try:
                print(f"Key: {key} (0x{key:02x}) -> {decrypted.decode()}")
            except:
                pass
  ```
- This tries every possible ascii bytes as key and xors it to get the output
  ```
    Key: 32 (0x20) -> 0n3_byt3_T0_ru1e_tH3m_4Ll
    Key: 33 (0x21) -> 1o2^cxu2^U1^st0d^uI2l^5Mm
    Key: 34 (0x22) -> 2l1]`{v1]V2]pw3g]vJ1o]6Nn
    Key: 35 (0x23) -> 3m0\azw0\W3\qv2f\wK0n\7Oo
    Key: 36 (0x24) -> 4j7[f}p7[P4[vq5a[pL7i[0Hh
    Key: 37 (0x25) -> 5k6Zg|q6ZQ5Zwp4`ZqM6hZ1Ii
    Key: 39 (0x27) -> 7i4Xe~s4XS7Xur6bXsO4jX3Kk
    Key: 40 (0x28) -> 8f;Wjq|;W\8Wz}9mW|@;eW<Dd
    Key: 41 (0x29) -> 9g:Vkp}:V]9V{|8lV}A:dV=Ee
    Key: 44 (0x2c) -> <b?Snux?SX<S~y=iSxD?aS8@`
    Key: 46 (0x2e) -> >`=Qlwz=QZ>Q|{?kQzF=cQ:Bb
    Key: 47 (0x2f) -> ?a<Pmv{<P[?P}z>jP{G<bP;Cc
    Key: 48 (0x30) ->  ~#Orid#OD Obe!uOdX#}O$\|
    Key: 52 (0x34) -> $z'Kvm`'K@$Kfa%qK`\'yK Xx
    Key: 53 (0x35) -> %{&Jwla&JA%Jg`$pJa]&xJ!Yy
    Key: 54 (0x36) -> &x%Itob%IB&Idc'sIb^%{I"Zz
    Key: 55 (0x37) -> 'y$Hunc$HC'Heb&rHc_$zH#[{
    Key: 56 (0x38) -> (v+Gzal+GL(Gjm)}GlP+uG,Tt
    Key: 57 (0x39) -> )w*F{`m*FM)Fkl(|FmQ*tF-Uu
    Key: 59 (0x3b) -> +u(Dybo(DO+Din*~DoS(vD/Ww
    Key: 60 (0x3c) -> ,r/C~eh/CH,Cni-yChT/qC(Pp
    Key: 62 (0x3e) -> .p-A|gj-AJ.Alk/{AjV-sA*Rr
    Key: 63 (0x3f) -> /q,@}fk,@K/@mj.z@kW,r@+Ss
  ```
- Now here only one plaintext seems to be understandable and it is key 32 (0x20)
- Hence the flag is **flag{0n3_byt3_T0_ru1e_tH3m_4Ll}**
