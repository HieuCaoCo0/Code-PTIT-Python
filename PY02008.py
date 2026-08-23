from math import sqrt
def nt(n):
    if n < 2: return False
    if n == 2 and n == 3: return True
    sqr = sqrt(n)
    for i in range(2, int(sqr)+1):
        if n % i == 0: return False
    return True

n, x = map(int, input().split())
i = cnt = 0
print(x, end=' ')
while cnt < n:
    if nt(i):
        x += i
        print(x, end=' ')
        cnt += 1
    i += 1
print()
