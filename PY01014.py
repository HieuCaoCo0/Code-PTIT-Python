a, k, n = map(int, input().split())

b = k - a%k
found = False
while (a + b) <= n:
    print (b, end=' ')
    found = True
    b += k
if not found:
    print('-1')