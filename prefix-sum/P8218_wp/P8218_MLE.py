n = int(input())  #序列长度
a = list(map(int, input().split()))  #n 个正整数 a₁, a₂, ⋯, aₙ
m = int(input())  #区间的数量
for _ in range(m):
    l, r = map(int, input().split())  #所求区间
    total = sum(a[l-1:r])   #区间求和，内存开销太大，MLE
    print(total)
