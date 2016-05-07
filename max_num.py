x = 8754365
digits = list()
num = x
while num > 0:
	digits.append(num%10)
	num = num/10
digits.sort()
num = 0
for i in range(len(digits)-1,-1,-1):
	num *= 10
	num += digits[i]	
print num