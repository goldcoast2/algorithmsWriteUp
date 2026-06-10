n, m = map(int, input().split())         #输入数目的数量和需要木材的总长度
trees = list(map(int, input().split()))  #每棵树的高度 
h = max(trees)                           #树的高度最大值
while True:
    #设置初始值为0
    total = 0
    for tree in trees:
        #只要某个树的高度大于h,砍下来的部分计入总数
        if tree > h:
            total += tree - h
    #总耗材大于或等于目标值，输出树的高度并且退出循环
    if total >= m:
        print(h)
        break
    #每次循环从最大值开始逐次-1
    h -= 1
