for t in range(int(input())):
    n = input()
    i = 0
    while i < 1000 and int(n) % 7 != 0:
        n = str(int(n) + int(n[::-1]))
        i += 1
    if int(n) % 7 == 0: print(n)
    else: print(-1) 