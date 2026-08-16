from math import sqrt
from array import array
from sys import stdin

n = int(stdin.readline())
a = array('i')
for i in range (n):
    x = int(stdin.readline())
    a.append(x)
    

# N, M = 1 + 2*(10**6), 2*(10**6)
# N, M = 1 + (10**6), (10**6)

M = max(a)
N = M + 1

U = array('i', [0]*N)
# sang uoc nt dau tien
for i in range(2, int(sqrt(M)) + 1):
    if U[i] == 0:
        U[i] = i
        for x in range(i*i, M+1, i):
            U[x] = i

# Quy hoach dong / Truy hoi
for i in range(4, N):
    # Mot thua so nt hay tong tca thua so nt
    U[i] += U[i//U[i]] if U[i] else i 

res = 0
for i in range (n):
    x = a[i]
    res += U[x]

print(res)