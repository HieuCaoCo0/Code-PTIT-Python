import math
def nt(n):
    if n < 2: return False
    if n == 2 or n == 3: return True
    sqr = int(math.sqrt(n))
    for i in range(2, sqr+1):
        if n % i == 0: return False
    return True

for t in range(int(input())):
    s = input()
    sum = 0
    for c in s:
        sum += int(c)

    if nt(sum): print('YES')
    else: print('NO')