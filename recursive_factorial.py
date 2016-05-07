def recursive_fact(n):
    if n == 1 or n == 0:
        return 1
    return n * recursive_fact(n-1)

print recursive_fact(int(raw_input()))
