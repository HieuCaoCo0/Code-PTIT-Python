n = int(input())
a = list(map(float, input().split()))
max_a, min_a = max(a), min(a)
while max_a in a: a.remove(max_a)
while min_a in a: a.remove(min_a)

avg = 0
for x in a: avg += x
avg /= len(a)

print(f'{avg:.2f}')