n = int(input())  #序列长度
a = list(map(int, input().split()))  #n 个正整数 a₁, a₂, ⋯, aₙ
m = int(input())  #区间的数量
for _ in range(m):
    l, r = map(int, input().split())  #所求区间
    s = 0
    #暴力求解区间和,时间复杂度太高，TLE
    for i in range(l-1, r):
        s += a[i]
    print(s)
