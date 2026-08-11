import math

# math.gcd(a, b)
def ucln(a, b):
    if b > 0:
        return ucln(b, a%b)
    else:
        return a
def nt(n):
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    sqr = int(math.sqrt(n))
    for i in range(2, sqr+1):
        if n % i == 0:
            return False
    return True

T = int(input())
for t in range(T):
    a, b = map(int, input().split())
    gcd = ucln(a, b)
    sum = 0
    while gcd > 0:
        sum += gcd % 10
        gcd //= 10
    if nt(sum):
        print('YES')
    else:
        print('NO')

