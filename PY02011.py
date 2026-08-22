n = int(input())
a = list(map(int, input().split()))
id, Min = 0, 1000000
for i in range(n):
    sum = 0
    for j in range(n):
        sum += abs(a[i]-a[j])
    if sum < Min:
        Min = sum
        id = i

print(Min, a[id])