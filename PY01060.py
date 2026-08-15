def sum_cs(s):
    sum = 0
    for i in range(1, len(s), 2):
        sum += int(s[i])
    return sum
def mul(s):
    res = 1
    found = False
    for i in range(0, len(s), 2):
        if s[i] != '0':
            res *= int(s[i])
            found = True
    if not found: return 0
    return res
        

for t in range(int(input())):
    s = input()
    print(f'{mul(s)} {sum_cs(s)}')