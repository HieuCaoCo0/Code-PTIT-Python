MAXN = 1100000
nt = [True]*MAXN
nt[0] = nt[1] = False
for i in range(2, int(MAXN**0.5)+1):
    if nt[i]:
        for j in range(i*i, MAXN, i):
            nt[j] = False

n = int(input())
a = list(map(int, input().split()))
dic = {}
for x in a:
    if nt[x]:
        if x not in dic: dic[x] = 1
        else: dic[x] += 1

for x in dic:
    print(x, dic[x])