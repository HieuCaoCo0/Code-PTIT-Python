def check(s):
    if len(s) % 2 != 0: return False
    if s != s[::-1]: return False
    for c in s:
        if ord(c) % 2 != 0: return False
    return True

for t in range(int(input())):
    n = int(input())
    for i in range (22, n, 2):
        if check(str(i)): print(i, end=' ')
    print()
    