for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    st, res = [], [0]*n # st chua index cua so chua tim thay phan tu tiep theo lon hon
    for i in range(n):
        while len(st) > 0 and a[st[-1]] <= a[i]:
            st.pop()
        if len(st) == 0: res[i] = i+1
        else: res[i] = i - st[-1]
        st.append(i)
    print(*res)
