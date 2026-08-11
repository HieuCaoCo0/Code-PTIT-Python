def thuanNgich(s):
    sum = 0
    for c in s:
        sum += int(c)
    string = str(sum)
    return sum >= 10 and string == string[::-1]


T = int(input())
for t in range(T):
    s = input()
    if thuanNgich(s):
        print('YES')
    else:
        print('NO')

