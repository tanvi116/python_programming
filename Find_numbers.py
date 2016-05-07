import re

handle = open('regex_sum_247978.txt')
text = handle.read()
total = 0
number = re.findall('[0-9]+',text)
if len(number) > 0:
    for item in number:
        num = float(item)
        total = total + num
print total