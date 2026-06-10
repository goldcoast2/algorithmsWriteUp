N,M=map(int,input().split())       #树木的数量和需要木材的总长度
an=list(map(int,input().split()))  #每棵树的高度
low,high=0,max(an)                 #锯片最低
ans=0                              #储存最终答案
# 定义检查函数：给定锯片高度 mid，计算能砍得的木材总长度
def check(an, mid):
    re = 0
    for i in range(N):           # 遍历每棵树
        if an[i] - mid > 0:      # 如果树比锯片高
            re += (an[i] - mid)  # 砍下超出部分
        # 否则该树无法砍到木材，加 0
    return re
# 二分查找模板：寻找最后一个使得砍得总长度 >= M 的高度
while low<=high:
    mid=(low+high)//2
    if check(an,mid)>=M:
        ans=mid
        low=mid+1  #缩小下界
    else:
        high=mid-1 #缩小上界
#得到最终答案
print(ans)
