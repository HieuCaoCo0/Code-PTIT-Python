import math
def nt(n):
    if n < 2: return False
    if n == 2 or n == 3: return True
    sqr = int(math.sqrt(n))
    for i in range(2, sqr+1):
        if n % i == 0: return False
    return True

def check(s):
    for i in range(len(s)):
        c = s[i]
        if c == '2' or c == '3' or c == '5' or c == '7':
            if not nt(i): return False
        else:
            if nt(i): return False
    return True

for t in range(int(input())):
    s = input()
    if check(s): print('YES')
    else: print('NO')