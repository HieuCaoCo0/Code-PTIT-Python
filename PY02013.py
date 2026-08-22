while True:
    n = int(input())
    if n == 0: break

    step = 1
    while n != 1:
        step += 1
        if n % 2 == 0: n /= 2
        else: n = n*3 + 1
    print(step)