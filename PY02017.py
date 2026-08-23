for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    dic = {}
    for x in a:
        if x not in dic:
            dic[x] = 1
        else:
            dic[x] += 1

    for x in dic:
        if dic[x] % 2 == 1:
            print(x)
            break