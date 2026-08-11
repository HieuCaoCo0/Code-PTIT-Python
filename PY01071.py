f = input().lower()
# print(f[-3::])
if len(f) >= 3 and f[-3:] == '.py':
    print('yes')
else:
    print('no')