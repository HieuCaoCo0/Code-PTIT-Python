for _ in range(int(input())):
    n = int(input())
    dict = {}
    cnt = 0
    for _ in range(n):
        x = int(input())
        if x in dict:
            dict[x] += 1
        else:
            dict[x] = 1
        cnt = max(cnt, dict[x])

    ans = 1000
    for i in dict:
        if dict[i] == cnt:
            ans = min(ans, i)
    print(ans)