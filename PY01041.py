def check(a):
    i = 1
    tang = giam = 0
    while i < len(a):
        if a[i] <= a[i-1]: break
        i += 1
    if i == len(a): return False
    while i < len(a):
        if a[i] >= a[i-1]: return False
        i += 1
    return True



for t in range(int(input())):
    s = input()
    print('YES' if check(s) else 'NO')