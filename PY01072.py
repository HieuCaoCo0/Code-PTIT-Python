n, k = map(int, input().split())
l = list(map(int, input().split()))
l = sorted(set(l))
a = [0]*(k+1)

n = len(l)

def Try(i):
    for j in range(a[i-1]+1, n-k+i+1):
        a[i] = j
        if i == k:
            for x in range(1, k+1):
                print(l[a[x]-1], end=' ')
            print()
        else: Try(i+1)

Try(1) 