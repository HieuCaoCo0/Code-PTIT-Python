import math
def nt(n):
    if n < 2: return False
    if n == 2 or n == 3: return True
    sqr = int(math.sqrt(n))
    for i in range(2, sqr+1):
        if n % i == 0: return False
    return True

def check(s):
    if not nt(len(s)): return False
    cnt = 0
    for c in s:
        if c == '2' or c == '3' or c == '5' or c == '7': 
            cnt += 1
    return cnt > (len(s)-cnt)

for t in range(int(input())):
    s = input()
    if check(s): print('YES')
    else: print('NO')