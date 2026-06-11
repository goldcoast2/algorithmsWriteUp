import math   #导入math库
M = int(input())  #正整数的值
limit = int(math.sqrt(2 * M))  #最大可能取值，这是一个等差数列求和公式
res = []               #列表存储数据
#从小到大依次尝试，中间部分是数学推导出来的
for y in range(2, limit + 1):
    if (2 * M) % y == 0:
        x = (2 * M) // y
        if x > y and (x - y + 1) % 2 == 0:
            a = (x - y + 1) // 2
            res.append((a, a + y - 1))
res.sort()#排序
for l, r in res:
    print(l, r)   #输出答案
