def lamTron(n):
    if n <= 10:
        return n
    p = 10
    while n > p:
        du = n % p
        if du >= p // 2:
            n += p-du
        else:
            n -= du
        p *= 10
    return n
    


T = int(input())
for t in range(T):
    n = int(input())
    print(lamTron(n))