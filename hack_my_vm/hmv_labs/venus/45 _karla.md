# Target User
denise  -pass: pFg92DpGucMWccA

# Method of Solve
- Login using the ssh credentials
- Perform ls -la to list all the files and cat the mission.txt
- use exiftool to look for the metadata and other comments and stuff in the image yuju.jpg
  ```
    karla@venus:~$ exiftool yuju.jpg 
    perl: warning: Setting locale failed.
    perl: warning: Please check that your locale settings:
    	LANGUAGE = (unset),
    	LC_ALL = (unset),
    	LANG = "en_US.UTF-8"
        are supported and installed on your system.
    perl: warning: Falling back to the standard locale ("C").
    ExifTool Version Number         : 12.57
    File Name                       : yuju.jpg
    Directory                       : .
    File Size                       : 33 kB
    File Modification Date/Time     : 2024:04:05 06:28:46+00:00
    File Access Date/Time           : 2024:04:05 06:28:46+00:00
    File Inode Change Date/Time     : 2024:04:05 06:29:46+00:00
    File Permissions                : -rw-r-----
    File Type                       : JPEG
    File Type Extension             : jpg
    MIME Type                       : image/jpeg
    JFIF Version                    : 1.01
    Resolution Unit                 : inches
    X Resolution                    : 96
    Y Resolution                    : 96
    Exif Byte Order                 : Big-endian (Motorola, MM)
    Artist                          : sML
    Date/Time Original              : 2021:11:01 10:34:51
    Create Date                     : 2021:11:01 10:34:51
    Sub Sec Time Original           : 95
    Sub Sec Time Digitized          : 95
    XP Author                       : sML
    Padding                         : (Binary data 2060 bytes, use -b option to extract)
    XMP Toolkit                     : Image::ExifTool 12.16
    About                           : pFg92DpGucMWccA
    Creator                         : sML
    Image Width                     : 442
    Image Height                    : 463
    Encoding Process                : Baseline DCT, Huffman coding
    Bits Per Sample                 : 8
    Color Components                : 3
    Y Cb Cr Sub Sampling            : YCbCr4:2:0 (2 2)
    Image Size                      : 442x463
    Megapixels                      : 0.205
    Create Date                     : 2021:11:01 10:34:51.95
    Date/Time Original              : 2021:11:01 10:34:51.95
  ```
- The Password is in author section
- The Password is **pFg92DpGucMWccA**

# Commands Used
- ls -la
- cat
- exiftool
