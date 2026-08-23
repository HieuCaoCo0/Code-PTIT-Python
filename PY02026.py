n, m = map(int, input().split())
a = set(map(int, input().split()))
b = set(map(int, input().split()))

if sorted(a&b) == sorted(a):
    print('YES')
else: print('NO')