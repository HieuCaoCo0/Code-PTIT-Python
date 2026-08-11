import math

T = int(input())
for t in range(T):
    n, x, m = map(float, input().split())

    year = math.ceil(
        math.log(m/n) / math.log(1+x/100)
        )
    print(year)