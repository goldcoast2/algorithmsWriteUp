M = int(input())   #正整数的值
left, right = 1, 1 #初始化左右指针
s = 0      #当前窗口所有数的和，初始为0
#右指针最大为M
while right <= M:
    #和小于M，放大窗口，右指针右移，总和加上右指针指向的值
    if s < M:
        s += right
        right += 1
    #和大于M，缩小窗口，左指针左移，总和减去左指针指向的值
    elif s > M:
        s -= left
        left += 1
    #和等于m，左右指针相差如果大于2，输出数对，总和减去左指针指向的值，左指针左移
    else:
        if right - left >= 2:
            print(left, right - 1)
        s -= left
        left += 1
