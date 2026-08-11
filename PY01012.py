s1 = input()
s2 = input()
n = int(input())
string = s1[:n-1:] + s2 + s1[n-1::]
print(string)