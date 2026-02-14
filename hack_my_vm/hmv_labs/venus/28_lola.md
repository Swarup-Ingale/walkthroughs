# Target User
celeste  -pass: VLSNMTKwSV2o8Tn

# Method of Solve
- Login using the ssh credentials
- Perform ls -la to list all the files and cat to read the mission.txt
- Then make a new directory in the /tmp folder and copy the pages.txt into it
- Use sed command to append .html to every line in the file
- Run the script given below to get the valid URL
- Use curl command to get the password from the URL
  ```
    sed 's/$/.html/' pages.txt > urls.txt

    cat urls.txt | xargs -I {} sh -c 'response=$(curl -s -o /dev/null -w "%{http_code}" http://localhost/{}); if [ "$response" -eq 200 ]; then echo "Valid endpoint found: http://localhost/{}"; else echo "Invalid or inaccessible endpoint: http://localhost/{} (HTTP $response)"; fi'

    curl -v http://localhost/cebolla.html
  ```

# Commands Used
- ls -la
- cat
- sed
- curl
