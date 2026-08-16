s1 = set(input().lower().split())
s2 = set(input().lower().split())

U = sorted(s1 | s2)
I = sorted(s1 & s2)

for w in U: print(w, end=' ')
print()
for w in I: print(w, end=' ')
print()


