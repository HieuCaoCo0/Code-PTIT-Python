T = int(input())
for t in range(T):
    s = input()
    cnt = 1
    for i in range(len(s) - 1):
        if s[i] == s[i+1]: cnt += 1
        else: 
            print(f'{cnt}{s[i]}', end='')
            cnt = 1
    print(f'{cnt}{s[-1]}', end='')
    print() 
