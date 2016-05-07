#https://www.hackerrank.com/challenges/coin-change

# Enter your code here. Read input from STDIN. Print output to STDOUT
a = raw_input().split()
c = list(map(int, raw_input().split()))
c.sort()

n = int(a[0])
m = int(a[1])

def change(n,coins_available,coins_so_far):    
    if sum(coins_so_far) == n:
        yield coins_so_far
    elif sum(coins_so_far) > n:
        pass
    elif coins_available == []:
        pass
    else:
        for c in change(n,coins_available[:],coins_so_far + [coins_available[0]]):            
            yield c
        for c in change(n,coins_available[1:],coins_so_far):            
            yield c

solutions = [s for s in change(n,c,[])]
ways = len(solutions)

print "No. of ways = ", ways
print "Optimal solution = ", min(solutions, key=len)
print "Minimum no. of coins required = ", len(min(solutions, key=len))
