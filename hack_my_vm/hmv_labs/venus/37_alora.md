# Target User
julie  -pass:sjDf4i2MSNgSvOv

# Method of Solve
- Login using the ssh credentials
- Perform ls -la to list all the files and cat mission.txt
- check file type of music.iso
- either cat the music.iso to get the password directly but you should be able to read the file contents
  ```
    alora@venus:~$ cat music.iso 
    CD001LINUX                           CDROM                           ��
    
    F                                                                                                                                                                                                                                                                                                                                                                                                GENISOIMAGE ISO 9660/HFS FILESYSTEM CREATOR (C) 1993 E.YOUNGDALE (C) 1997-2006 J.PEARSON/J.SCHILLING (C) 2006-2007 CDRKIT TEAM                                                                                                                 2024040506284600202404050628460000000000000000002024040506284600                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                �CD00|.SP��RR�PX$mAAmTF␦|.|.|.CE�|.RR�PX$mAAmTF␦|.|.|.~��|.
                                                                                                                                 MUSIC.ZIP;1RR�NMmusic.zipPX$$��$TF␦|.|.|.ER�
    T�RRIP_1991ATHE ROCK RIDGE INTERCHANGE PROTOCOL PROVIDES SUPPORT FOR POSIX FILE SYSTEM SEMANTICSPLEASE CONTACT DISC PUBLISHER FOR SPECIFICATION SOURCE.  SEE PUBLISHER IDENTIFIER IN PRIMARY VOLUME DESCRIPTOR FOR CONTACT INFORMATION.PK
    �3�X�h��pwned/alora/music.txtUT	�f�fux
                                          sjDf4i2MSNgSvOv
    PK
    �3�X�h����pwned/alora/music.txtUT�fux
                                         PK[_
  ```
- OR
- cat the file contents in base_64 and then save it to our local machine as music.b64
- Then Open it manually and cat the music.txt
- The password is **sjDf4i2MSNgSvOv**

# Commands Used
- ls -la
- cat
- base64
- file
