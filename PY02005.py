n = int(input())
A = list(map(int, input().split()))
res = 0
for i in range(n-1):
    for j in range(i+1, n):
        if A[i] > A[j]: res += 1
print(res)