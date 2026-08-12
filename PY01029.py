import math

for t in range(int(input())):
    n = input()
    b = int(n[::-1])
    a = int(n)

    if math.gcd(a, b) == 1: print('YES')
    else: print('NO')

