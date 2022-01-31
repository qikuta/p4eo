from bs4 import BeautifulSoup
import urllib.request, urllib.parse, urllib.error

# http://www.dr-chuck.com/page1.htm

url = input("Enter URL: ")
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all the anchor tags
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))
