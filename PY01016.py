T = int(input())
for t in range(T):
    s = input()
    i = 0
    while i < len(s):
        for j in range(int(s[i+1])):
            print(s[i], end='')
        i+=2
    print()