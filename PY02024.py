from functools import cmp_to_key

def tong_cs(n):
    if n == 0: return 0
    res = 1
    while n > 0:
        res *= n % 10
        n //= 10
    return res

def cmp(a, b):
    sum_a, sum_b = tong_cs(a), tong_cs(b)
    if sum_a == sum_b: return a - b
    return sum_a - sum_b

for _ in range(int(input())):
    n = int(input())
    a = sorted(
        list(map(int, input().split())),
        key=cmp_to_key(cmp)
    )
    print(*a)