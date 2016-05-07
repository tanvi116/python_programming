#code
def find_smallest(n):
    d = [i for i in n]
    rev_d = list(reversed(sorted(d)))    
    if d == rev_d:
        print "not possible"
    else:
        x = len(d) - 1
        while x > 0:
            if d[x] > d[x-1]:
                break
            else:
                x -= 1
        large = d[x]
        small = d[x-1]
        
        ind = x
        for i in range(x,len(d)):
            if large > d[i] > small:
                large = d[i]
                ind = i
        (d[x-1],d[i]) = (d[i],d[x-1])
        d[x:] = sorted(d[x:])
        print "".join(str(i) for i in d)

for _ in range(int(raw_input())):
    n = raw_input()
    find_smallest(n)
