#https://www.hackerrank.com/challenges/coin-change

# Enter your code here. Read input from STDIN. Print output to STDOUT
a = raw_input().split()
c = list(map(int, raw_input().split()))
c.sort()

n = int(a[0])
m = int(a[1])

def coinChange(n,c):
    counts = [1] + [0] * n
    print counts
    for i in c:
        for j in range(len(counts)):
            if i + j <= n:
                counts[i + j] += counts[j]
                print counts
    return counts[-1]

print coinChange(n,c)
