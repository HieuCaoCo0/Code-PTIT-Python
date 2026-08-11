T = int(input())
for t in range(T):
    s = input()
    if s[-2::] == '86': print('YES')
    else: print('NO')