M=int(input())               #正整数的值
an=[_ for _ in range(1,M)]   #构造从1到M-1的数列
for l in range(1, M):
    for r in range(l, M):
        #穷举构造数列，如果求和等于M，则输出
        if sum(an[l:r]) == M:
            print(an[l],an[r-1])
