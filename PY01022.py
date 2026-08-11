def step(s):
    if len(s) == 1: return 0
    sum = 0
    for c in s: sum += ord(c) - ord('0')
    return 1 + step(str(sum))


s = input()
# if s[0] == '-':
#     s = s[1::]
if len(s) <= 1: print(1)
else: print(step(s))
