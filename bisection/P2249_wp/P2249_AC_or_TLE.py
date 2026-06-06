n, m = map(int, input().split())      #数字个数和询问次数
a = list(map(int, input().split()))   #待查询的数字
qs = list(map(int, input().split()))  #询问这些数字的编号
out = []                              #存放数据
for x in qs:
    l, r = 0, n - 1                   #左右区间起点
    ans = -1                          #编号从-1开始
    while l <= r:
        mid = (l + r) // 2            #对半查找
        if a[mid] >= x:
            ans = mid                 #更新编号
            r = mid - 1               #如果大于等于目标值，就缩小右区间，由于是左边第一个最大值，等于号放在缩小右区间这里
        else:
            l = mid + 1               #如果小于目标值，就缩小左区间
    #如果查询到就添加编号
    if ans != -1 and a[ans] == x:
        
        out.append(str(ans + 1))
    else:
        out.append("-1")
print(*out)                           #输出在序列中第一次出现的编号（没有就输出-1）
