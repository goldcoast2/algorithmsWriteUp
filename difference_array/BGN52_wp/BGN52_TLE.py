n, m = map(int, input().split())     #元素数量和操作次数
an = list(map(int, input().split())) #n个整数 a₁, a₂, ⋯, aₙ
for _ in range(m):
    l, r, k = map(int, input().split())  #表示区间[l,r]各个元素+k
    #每次操作都要从l-1到r-1循环更新，时间复杂度太高，TLE
    for i in range(l-1, r):
        an[i] += k
 
print(*an)
