n = int(input())  #序列长度
a = list(map(int, input().split()))  #n 个正整数 a₁, a₂, ⋯, aₙ
m = int(input())  #区间的数量
pre=[0]*(n+1)  #初始化前缀和数列
for j in range(n):
    pre[j+1]=pre[j]+a[j]   #构造前缀和数列
for _ in range(m):
    l,r=map(int,input().split())  #所求区间
    print(pre[r]-pre[l-1])  #两项相减就是所求区间子段和
