import urllib

conn = urllib.urlopen("http://www.pythonlearn.com/code/intro-short.txt")

print conn

for line in conn:
    print line.rstrip()