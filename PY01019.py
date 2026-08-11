def check(s1, s2):
    for i in range(len(s1)):
        dis1 = abs(ord(s1[i]) - ord(s1[i-1]))
        dis2 = abs(ord(s2[i]) - ord(s2[i-1]))
        if dis1 != dis2: return False
    return True

T = int(input())
for t in range(T):
    s1 = input()
    s2 = s1[::-1]
    if check(s1, s2): print('YES')
    else: print('NO')