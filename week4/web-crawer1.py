# why you want to do crawling ?
#1. Pull data: particularly social data
#2. Get your own data back out of the some system that has no 'export capability'
#3. Monitor a site for new information
#4. Spider the web to make a database for a search engine
# or just learning like me :D
# to install Beatiful Soup:
# windows: pip install beautifulsoup4
# Ubuntu/Linux: apt-get install python-bs4

import requests
import urllib
from bs4 import BeautifulSoup

url = raw_input('Enter - ')
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)
#retrieve a list of anchor tags
# each tag is like a dictionary of HTML attributes

tags = soup('a')
for tag in tags:
    print tag.get('href', None)
    
