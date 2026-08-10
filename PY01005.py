def lucky(s):
    cnt = 0
    for c in s:
        if int(c) == 4 or int(c) == 7:
            cnt += 1
    if cnt == 4 or cnt == 7:
        return True
    return False

s = input()
if lucky(s):
    print('YES')
else:
    print('NO')