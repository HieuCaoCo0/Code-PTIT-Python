import math
def nt(n):
    if n < 2: return False
    if n == 2 or n == 3: return True
    sqr = int(math.sqrt(n))
    for i in range (2, sqr):
        if n % i == 0: return False
    return True

for t in range(int(input())):
    s = input()
    dau = s[0:3].lstrip('0')
    cuoi = s[-3::].lstrip('0')
    if nt(int(dau)) and nt(int(cuoi)):
        print('YES')
    else: print('NO')