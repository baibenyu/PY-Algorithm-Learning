# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/3/11 13:36'

n, s = map(int, input().strip().split())
# 方法一:枚举
i = 1
while True:
    j = n
    able = i
    sum_up = i
    while j > 0:
        able = able * 2 - 1
        sum_up = sum_up + able
        j -= 1
    if sum_up == s:
        break
    else:
        i += 1
print(i)

# 方法二:数学归纳法
# 每年新增人数=2*上一年新增人数-1,总人数=每一年的新增人数累加,最终得到一个等差乘等比的通项公式,乘公比错位相减
print((s-2-n+2**(n+1))//(2**(n+1)-1))