# Targer User
iris  -pass: kYjyoLcnBZ9EJdz 

But here we are using another approach to get direct access to shell using the open ssh key of iris

# Method of Solve
- Login using the ssh credentials
- Perform ls -la to list all the files and cat the mission.txt
- Cat the .iris_key to see what it is ... it is the ssh key for iris shell
  ```
    eliza@venus:~$ ssh iris@localhost -i .iris_key
  ```
- Get direct access to the iris users shell

# Commands Used
- ls -la
- cat
- ssh
