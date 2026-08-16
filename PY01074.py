from math import sqrt
from array import array

N, M = 1 + 2*(10**6), 2*(10**6)
U = array('i', [0]*N)
# sang uoc nt dau tien
for i in range(2, int(sqrt(M)) + 1):
    if U[i] == 0:
        U[i] = i
        for u in range (i, M//i + 1):
            U[i*u] = i

# Quy hoach dong / Truy hoi
for i in range(4, N):
    # Mot thua so nt hay tong tca thua so nt
    U[i] += U[i//U[i]] if U[i] else i 

from sys import stdin
res = 0
n = int(stdin.readline())
while n:
    try:
        x = int(stdin.readline())
        res += U[x]
        n -= 1
    except: break

print(res)