# nt = [True]*1005
# for i in range(2, int(1005**0.5)+1):
#     if nt[i]:
#         for j in range (i*i, 1005, i):
#             nt[j] = False
# nt[0] = nt[1] = False

# n, x = map(int, input().split())

# i = 0
# cnt = 0
# print(x, end=' ')
# while i < 1001 and cnt < n:
#     if nt[i]:
#         x += i
#         print(x, end=' ')
#         cnt += 1
#     i += 1
# print()

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
