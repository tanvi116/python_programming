import urllib
import xml.etree.ElementTree as ET

address = raw_input('Enter location:')
uh = urllib.urlopen(address)
data = uh.read()
print 'Retrieving',address
print 'Retrieved',len(data),'characters'
tree = ET.fromstring(data)
results = tree.findall(".//count")
print "Count:", len(results)
total = 0
for i in results:
    total += int(i.text)
print "Sum:",total
