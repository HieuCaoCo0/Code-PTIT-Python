import math

def nt(n):
    if n < 2: return False
    if n == 2 and n == 3: return True
    sqr = int(math.sqrt(n))
    for i in range(2, sqr+1):
        if n % i == 0: return False
    return True

for t in range(int(input())):
    s = input()
    n = s[-4::]
    while len(n) > 1 and n[0] == '0': n = n[1::]
    if nt(int(n)): print('YES')
    else: print('NO')
