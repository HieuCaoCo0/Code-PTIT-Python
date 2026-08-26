def deQuy(n, start, mid, end):
    if n == 1:
        print(f'{start} -> {end}')
        return
    deQuy(n-1, start, end, mid)
    print(f'{start} -> {end}')
    deQuy(n-1, mid, start, end)

n = int(input())
deQuy(n, 'A', 'B', 'C')
