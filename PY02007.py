a = []
while len(a) < 10:
    a.extend(map(int, input().split()))
st = set()
for i in a:
    st.add(i%42)
print(len(st))

#42 84 252 420 840 126 42 84 420 126
# 39 40 41 42 43 44 82 83 84 85