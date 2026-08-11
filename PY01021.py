T = int(input())
for t in range(T):
    s = input()
    srt = ''.join(sorted(s))
    sum = 0
    for c in srt:
        if c.isdigit():
            sum += int(c)
        else:
            print(c, end='')
    print(sum)