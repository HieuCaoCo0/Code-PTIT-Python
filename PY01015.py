def koGiam(s):
    for i in range(1, len(s)):
        n1 = int(s[i])
        n2 = int(s[i-1])
        if n1 < n2:
            return False
    return True

T = int(input())
for t in range(T):
    s = input()
    if koGiam(s):
        print('YES')
    else:
        print('NO')