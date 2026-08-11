s = input()
chuThuong = 0
chuHoa = 0
for c in s:
    if c.isupper():
        chuHoa += 1
    elif c.islower():
        chuThuong += 1
if chuHoa > chuThuong:
    print(s.upper())
else:
    print(s.lower())