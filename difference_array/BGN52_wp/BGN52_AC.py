n, m = map(int, input().split())     #元素数量和操作次数
an = list(map(int, input().split())) #n个整数 a₁, a₂, ⋯, aₙ
#初始化差分数列，差分数列首项为原数列首项
diff = [0] * (n + 1)            
diff[0] = an[0]
for i in range(1, n):
    diff[i] = an[i] - an[i - 1]  #构造差分数列
for _ in range(m):
    l, r, k = map(int, input().split())  #表示区间[l,r]各个元素+k
    diff[l - 1] += k    #差分数列第l-1项+k
    diff[r] -= k        #差分数列列第r项+k
#初始化前缀和数列来还原，前缀和数列首项为原数列首项
score = [0] * n         
score[0] = diff[0]   
for i in range(1, n):
    score[i] = score[i - 1] + diff[i]    #用前缀和还原数列
print(*score)   #还原的数列就是所求数列
