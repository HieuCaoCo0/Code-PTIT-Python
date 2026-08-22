for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    dic = {}
    for x in a:
        if x not in dic:
            dic[x] = 1
        else:
            dic[x] += 1

    Max = -1
    res = 0
    for x in dic:
        if dic[x] > Max:
            Max = dic[x]
            res = x
    if Max > n/2: print(res)
    else: print('NO')