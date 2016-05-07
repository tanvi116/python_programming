#https://www.hackerrank.com/challenges/sparse-arrays

n = int(raw_input().strip())
n_list = []
for i in range(n):
    n_list.append((raw_input()))
q = int(raw_input().strip())
q_list = []
for i in range(q):
    q_list.append((raw_input()))
for i in range(q):
    print sum([1 for j in range(n) if n_list[j] == q_list[i]])
