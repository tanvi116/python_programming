# Enter your code here. Read input from STDIN. Print output to STDOUT
t = int(raw_input())
for x in range(t):
    n = int(raw_input())
    a = raw_input()
    arr = a.split()
    arr = list(map(int,arr))

    max_sum1 = 0
    max_sum2 = 0
    max1 = arr[0]
    sum1 = 0

    for i in arr:
        if max1 < i:
            max1 = i
        sum1 += i
        if i > 0:
            max_sum1 += i
        if max_sum2 < sum1:
            max_sum2 = sum1
        if sum1 < 0:
            sum1 = 0

    if max_sum1 <= 0:
        max_sum1 = max1
    if max_sum2 <= 0:
        max_sum2 = max1
    print max_sum2, max_sum1
