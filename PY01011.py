def beauti(s):
    if len(s) % 2 != 0:
        return False
    for c in s:
        if int(c) % 2 != 0:
            return False
    for i in range(len(s) // 2):
        if s[i] != s[-i-1]:
            return False
    return True

dep = []
for i in range (22, 1000000):
    if beauti(str(i)):
        dep.append(i)

T = int(input())
for t in range(T):
    n = int(input())
    i = 0
    while i < len(dep) and dep[i] < n:
        print(dep[i], end=' ')
        i += 1
    print()