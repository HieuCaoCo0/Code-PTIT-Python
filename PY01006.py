def lucky(s):
    for c in s:
        if int(c) != 4 and int(c) != 7:
            return False
    return True

T = int(input())
for t in range(T):
    s = input()
    if lucky(s):
        print('YES')
    else:
        print('NO')