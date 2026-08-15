import math
def nt(n):
    if n < 2: return False
    if n == 2 or n == 3: return True
    sqr = int(math.sqrt(n))
    for i in range(n, sqr+1):
        if n % i == 0: return False
    return True

def check(s):
    sum = 0
    for i in range(len(s)):
        sum += int(s[i])
        if i % 2 == 0:
            if int(s[i]) % 2 != 0: return False
        else:
            if int(s[i]) % 2 == 0: return False
    return nt(sum)

for t in range(int(input())):
    s = input()
    if check(s): print('YES')
    else: print('NO')