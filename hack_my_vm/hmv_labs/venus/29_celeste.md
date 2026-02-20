# Target User
nina  -pass: ixpeqdWuvC5N9kG

# Method of Solve
- Login using the ssh credentials
- Perform ls -la to list all the files and cat mission.txt to read the mission
- login to the mysql mariadb database using the celeste credentials
  ```
    celeste@venus:~$ mysql -u celeste -p 
    Enter password: 
    Welcome to the MariaDB monitor.  Commands end with ; or \g.
    Your MariaDB connection id is 81
    Server version: 10.11.6-MariaDB-0+deb12u1 Debian 12
    
    Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.
    
    Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.
    
    MariaDB [(none)]>
  ```
- Then Perform operation to show databases and select the venus database anad search for all the tables in the database venus
  ```
    MariaDB [(none)]> show databases;
    +--------------------+
    | Database           |
    +--------------------+
    | information_schema |
    | venus              |
    +--------------------+
    2 rows in set (0.007 sec)
    
    MariaDB [(none)]> use venus;
    Reading table information for completion of table and column names
    You can turn off this feature to get a quicker startup with -A

    MariaDB [venus]> show tables;
    +-----------------+
    | Tables_in_venus |
    +-----------------+
    | people          |
    +-----------------+
    1 row in set (0.002 sec)
    Database changed
    MariaDB [venus]>
  ```
- Then lets select the peoples table and print all the users and passwords in it
  ```
    MariaDB [venus]> select * from people
        -> ;
    +-----------+---------------+--------------------------------+
    | id_people | uzer          | pazz                           |
    +-----------+---------------+--------------------------------+
    |         1 | nuna          | ixpfdsvcxeqdW                  |
    |         2 | nona          | ixpvcxvcxeqdW                  |
    |         3 | manue         | ixpfdsfdseqdW                  |
    .                                                            .
    .                                                            . 
    .                                                            .  
    .                                                            .
    .                                                            .
    |        95 | nina         | ixpeqdWuvC5N9kG                 |
    +-----------+---------------+--------------------------------+
    95 rows in set (0.010 sec)
  ```
- The user we want is ninna

# Commands Used
- ls -la
- cat
- mysql queries
