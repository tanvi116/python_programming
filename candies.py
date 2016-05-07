# Enter your code here. Read input from STDIN. Print output to STDOUT
#https://www.hackerrank.com/challenges/candies
n = int(raw_input())
rating = []
for i in range(n):
    rating.append(int(raw_input()))

candy = [1]*n

def checkCandy(rating,candy, n):
    for i in range(1,n):
        if rating[i - 1] < rating[i]:
            yield candy[i - 1] + 1
        elif rating[i - 1] > rating[i]:
            candy[i] = candy[i-1] + 1
            yield candy[i]
            yield checkCandy(rating,candy,i)            

candy = [i for i in checkCandy(rating,candy,n)]

print candy
print sum(candy)
