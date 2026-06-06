n, m = map(int, input().split())      #数字个数和询问次数
a = list(map(int, input().split()))   #待查询的数字
qs = list(map(int, input().split()))  #询问这些数字的编号
res = []                              #存放数据
for q in qs:
    ans = -1                          #编号从-1开始
    for i in range(n):
        #如果查询到就更新编号
        if a[i] == q:
            ans = i + 1
            break
    res.append(str(ans))              #添加编号
print(' '.join(res))                  #输出在序列中第一次出现的编号（没有就输出-1）
