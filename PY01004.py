import math

def nt(n):
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    sqr  = int(math.sqrt(n))
    for i in range(2,sqr+1):
        if n % i == 0:
            return  False
    return True

T = int(input())
for t in range(T):
    n = int(input())
    cnt = 0
    for i in range(1, n):
        if math.gcd(n, i) == 1:
            cnt += 1
    if nt(cnt):
        print('YES')
    else:
        print('NO')