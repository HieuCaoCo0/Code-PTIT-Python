T = int(input())
for t in range(T):
    s = input()
    # print(f'({s[0:2:]} {s[-2::]})')
    if s[0:2:] == s[-2::]:
        print('YES')
    else:
        print('NO')