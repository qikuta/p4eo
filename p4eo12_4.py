"""
Exercise 4: Change the urllinks.py program to extract and count paragraph (p)
tags from the retrieved HTML document and display the count of the paragraphs
as the output of your program. Do not display the paragraph text, only count them.
Test your program on several small web pages as well as some larger web pages.
"""
from bs4 import BeautifulSoup
import urllib.request, urllib.parse, urllib.error

# test URLs below
# http://www.dr-chuck.com/page1.htm
# http://data.pr4e.org/romeo-full.txt

url = input("Enter URL: ")
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

count = 0
# Retrieve all the anchor tags
tags = soup('p')
for tag in tags:
    count += 1

print(f'Number of paragraphs: {count}')
