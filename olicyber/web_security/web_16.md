# URL
https://training.olicyber.it/challenges#challenge-355

# Concept
To navigate through multiple connected pages and snoop their HTML source codes to get the required data 

# Method of Solve
- Go to the Challenge Interface and copy the Target URL
- Lets write a python Script to snoop through all the Pages that are referenced in the provided target URL
- Then find the page that contains the data, here flag
  ```
    import requests
    from bs4 import BeautifulSoup
    from urllib.parse import urljoin, urlparse
    
    def check_flag_in_h1(soup):
        h1 = soup.find('h1')
        if h1:
            testing = h1.get_text(strip=True)
            if "flag{" in testing:
                return testing
        return None
    
    def crawl_and_find_flag(url, visited=None):
        if visited is None:
            visited = set()
    
        parsed = urlparse(url)
        url_normalized = f"{parsed.scheme}://{parsed.netloc}{parsed.path}"
        if parsed.query:
            url_normalized += f"?{parsed.query}"
    
        if url_normalized in visited:
            return None
        visited.add(url_normalized)
        
        print("Visited:", url_normalized)
        
        try:
            response = requests.get(url)
            response.raise_for_status()
            page_html = response.text
            soup = BeautifulSoup(page_html, 'html.parser')
            
            flag = check_flag_in_h1(soup)
            if flag:
                print("Flag found:", flag)
                return flag
            
            for a in soup.find_all('a', href=True):
                link_url = urljoin(url, a['href'])
                if urlparse(link_url).netloc == urlparse(url).netloc:
                    flag_found = crawl_and_find_flag(link_url, visited)
                    if flag_found:
                        return flag_found
        except requests.RequestException as e:
            print(f"Error in crawling the {url}: {e}")
        
        return None
    
    url_base = "http://web-16.challs.olicyber.it/"
    flag = crawl_and_find_flag(url_base)
    
    if flag:
        print("The flag is :", flag)
  ```
- The Flag is **flag{n0wh3r3_i5_54f3}**
    else:
        print("Flag not found.")
