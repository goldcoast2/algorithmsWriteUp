w = int(input())    #每组纪念品价格之和的上限
n = int(input())    #购来的纪念品的总件数
prices = []         #存储价格
for _ in range(n):
    prices.append(int(input()))  #输入价格
prices.sort()      #排序
#设置左右指针及目标答案
left = 0
right = n - 1
ans = 0
#当左指针小于右指针时，如果左右指针所对应的数加起来小于等上限，左指针往右，右指针往左
while left <= right:
    if prices[left] + prices[right] <= w:
        left += 1
        right -= 1
    #否则只有右指针往左
    else:
        right -= 1
    #每轮循环都将答案＋1
    ans += 1
print(ans)           #输出最后的结果

