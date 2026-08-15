for t in range(int(input())):
    s = input()
    mul = 1
    for c in s:
        if c != '0':
            mul *= int(c)

    print(mul)