import json
import urllib

address = raw_input('Enter location:')
uh = urllib.urlopen(address)
data = uh.read()

print 'Retrieving',address
print 'Retrieved',len(data),'characters'

info = json.loads(data)
count = 0
total = 0

for item in info["comments"]:
    if item["count"]:
        count += 1
        total += item["count"]

print "Count:", count
print "Sum:",total
