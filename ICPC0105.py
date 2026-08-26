import re
for _ in range(int(input())):
    s = input()
    a = re.findall(r'\d+', s)
    print(max(map(int, a)))



# for _ in range(int(input())):
#     s = input()
#     num = []
#     i = start = 0
#     while i < len(s):
#         if s[i].isdigit(): i+=1
#         else:
#             if start < i: num.append(int(s[start:i]))
#             i += 1
#             start = i
#     if start < len(s): num.append(int(s[start]))
#     print(max(num))

