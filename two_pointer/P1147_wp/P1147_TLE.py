M = int(input()) #正整数的值
pre = [0] * (M + 2)#构造前缀和数列
for i in range(1, M + 1):
    pre[i] = pre[i-1] + i
for l in range(1, M + 1):
    for r in range(l + 1, M + 1):
        #穷举前缀和数列，如果总和等于M，则输出
        if pre[r] - pre[l-1] == M:
            print(l, r)
