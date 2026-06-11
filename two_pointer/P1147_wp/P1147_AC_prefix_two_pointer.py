M = int(input())       #正整数的值
# 构造前缀和数组
pre = [0] * (M + 2)
for i in range(1, M + 1):
    pre[i] = pre[i-1] + i
#设置左指针和又指针
left = 0
right = 1
# right 最大到 M，且保证左指针小于右指针
while left < right and right <= M:  
    current_sum = pre[right] - pre[left]
    #如果等于给定正整数的值
    if current_sum == M:
        # 至少要两个数，所以 right - left >= 2
        if right - left >= 2:  
            print(left + 1, right)#输出两个端点
        left += 1  # 移动左指针继续找
    #如果小于M，右指针移动
    elif current_sum < M:
        right += 1
    #如果等于M，左指针移动
    else:
        left += 1
        #当 left 追上了 right，需要重置 right
        if left >= right:
            right = left + 1
