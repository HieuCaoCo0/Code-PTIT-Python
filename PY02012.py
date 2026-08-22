n = int(input())
a = []
while len(a) < n:
    a.extend(list(map(int, input().split())))
chan = []
le =[]
for x in a:
    if x % 2 == 0: chan.append(x)
    else: le.append(x)

chan.sort()
le.sort(reverse=True)
i_chan = i_le = 0
for x in a:
    if x % 2 == 0:
        print(chan[i_chan], end=' ')
        i_chan += 1
    else:
        print(le[i_le],end=' ')
        i_le += 1
