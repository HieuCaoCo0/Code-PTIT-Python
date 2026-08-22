n = int(input())
a = list(map(int, input().split()))
found = False
# if a[0] != 1:
#     print(1)

for i in range(1, n+2):
    if i not in a:
        print(i)
        break