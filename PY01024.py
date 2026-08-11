def check(s):
    # if len(s) % 10 != 0: return False
    sum = 0
    for c in s: sum += ord(c) - ord('0')
    if sum % 10 != 0: return False
    for i in range (1, len(s)):
        n1 = ord(s[i]) - ord('0')
        n2 = ord(s[i-1]) - ord('0')
        diff = abs(n1-n2)
        if diff != 2: return False;
    return True

T = int(input())
for t in range(T):
    s = input()
    if check(s): print('YES')
    else: print('NO')