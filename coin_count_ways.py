# Enter your code here. Read input from STDIN. Print output to STDOUT
#https://www.hackerrank.com/challenges/coin-change

# Enter your code here. Read input from STDIN. Print output to STDOUT
a = raw_input().split()
c = list(map(int, raw_input().split()))
c.sort()

n = int(a[0])
m = int(a[1])

memo = {}

def coinChange(n,c):
    global memo
   
    if n == 0:
        return 1
    elif n < 0:
        return 0
    elif len(c) == 0:
        return 0
    elif (n,len(c)) in memo:        
        return memo[(n,len(c))]
    else:
        memo[(n,len(c))] = sum([coinChange(n - (c[0] * i),c[1:]) for i in range(n/c[0] + 1)])
        return memo[(n,len(c))]
    
print coinChange(n,c)
