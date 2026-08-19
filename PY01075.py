from sys import stdin
from math import gcd

for t in range(int(stdin.readline())):
    dp = {0:0} # cost nho nhat cua dp[i] (gcd = i)
    ucln = [0] # cac gcd da tinh duoc tu cac gia tri trong mang A

    n = int(stdin.readline())
    A = list(map(int, stdin.readline().split()))
    C = list(map(int, stdin.readline().split()))

    for i in range(n):
        for p in ucln:
            tmp = gcd(p, A[i])
            cost = dp[p] + C[i]
            if tmp not in dp:
                dp[tmp] = cost
                ucln.append(tmp)
            elif dp[tmp] > cost:
                dp[tmp] = cost

    if 1 not in dp:
        dp[1] = -1

    print(dp[1])
                
            
    
