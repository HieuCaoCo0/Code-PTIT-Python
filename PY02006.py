def check(a, b):
    x = sorted(a)
    y = sorted(b)
    for i in range(len(a)):
        if x[i] > y[i]: return False
    return True

for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    if check(a, b): print('YES')
    else: print('NO')