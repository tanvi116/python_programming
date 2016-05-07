def iterative_fact(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i
    print fact

iterative_fact(int(raw_input()))
