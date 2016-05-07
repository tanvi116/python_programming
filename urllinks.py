# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
from BeautifulSoup import *

url = raw_input('Enter URL: ')
count = raw_input('Enter count: ')
count_num = int(count)
pos = raw_input('Enter position: ')
position = int(pos)

html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)
# Retrieve all of the anchor tags
tags = soup('a')
print "Retrieving: ",url

for i in range(0,count_num):    
    url = tags[position-1].get('href',None)
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
    # Retrieve all of the anchor tags
    tags = soup('a')
    print "Retrieving: ",url
    
