try:
    import urllib.parse as upas
    import urllib.request
    import requests
    import pandas as pd
    from bs4 import BeautifulSoup as bs

except ImportError:    
    print("İmport error, get.py")

def get_in(url):
    response = requests.get(url)
    in_html = response.content
    soup = bs(in_html,"html.parser")
    paragraph = soup.find_all('p')

    return paragraph

def convert(site):
    
    #contents = urllib.request.urlopen(site).read()
    #contents = site
    #encoding = "utf-8"
    #contents = contents.decode(encoding)
    
    contents = upas.quote(site)
    return contents