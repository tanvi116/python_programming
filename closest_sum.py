# Enter your code here. Read input from STDIN. Print output to STDOUT
for _ in range(int(raw_input())):
    n = int(raw_input().strip())
    arr = list(map(int,raw_input().strip().split()))

    arr.sort()
    
    total = abs(arr[1]+arr[0])
    x = [arr[0], arr[1]]       

    for i in range(n-1):
        if abs(arr[i+1]+arr[i]) < total:
            total = abs(arr[i+1]+arr[i])
            x =[arr[i], arr[i+1]]        
    print x[0],x[1]
