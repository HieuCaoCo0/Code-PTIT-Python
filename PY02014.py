MAXN = 100000
nt, NT = [], [True] * MAXN
NT[0] = NT[1] = False
for i in range(2, int(MAXN**0.5)+1):
    if NT[i]:
        for j in range(i*i, MAXN, i):
            NT[j] = False
for i in range(MAXN):
    if NT[i]: nt.append(i)


n = int(input())
a = list(map(int, input().split()))
Max = 0
for i in a:
    m = nt[-1]
    for j in nt: m = min(m, abs(j-i))
    Max = max(Max, m)

print(Max)