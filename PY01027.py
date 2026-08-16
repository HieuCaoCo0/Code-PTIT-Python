def check(s):
    i = 0
    while i < len(s):
        if s[i:i+3] == '688': i += 3
        elif s[i:i+2] == '68': i += 2
        elif s[i] == '6': i += 1
        else: return False
    return True

s = input()

print('YES' if check(s) else 'NO')
        