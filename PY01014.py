a, k, n = map(int, input().split())

b = 1
found = False
while (a + b) <= n:
    if (a + b) % k == 0:
        print (b, end=' ')
        found = True
if not found:
    print('-1')