P = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_.'

while True:
    st = input()
    if st == '0': break

    k, s = st.split()
    k = int(k)
    res = ''

    for c in s:
        idx = P.find(c)
        res += P[(idx+k)%28]
    print(res[::-1])