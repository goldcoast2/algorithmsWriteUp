import bisect                             #导入bisect库
n, m = map(int, input().split())          #数字个数和询问次数
a = list(map(int, input().split()))       #待查询的数字
queries = list(map(int, input().split())) #询问这些数字的编号
for item in queries:
    left=bisect.bisect_left(a,item)       #查找有序数组a中item元素第一次出现的位置并返回索引值
    #由于如果要找的数字不存在,会返回一个应该插入的位置索引，以保持列表的有序性,所以需要判断下标是否有效
    if a[left]==item:
        print(left+1,end=' ')
    else:
        print(-1,end=' ')
