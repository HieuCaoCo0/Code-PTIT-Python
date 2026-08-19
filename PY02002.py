F = [0]*93
F[0], F[1] = 0, 1

for i in range(2, 93):
    F[i] = F[i-1]+F[i-2]

for t in range(int(input())):
    l, r = map(int, input().split())
    for i in range(l, r+1):
        print(F[i], end=' ')
    print()


