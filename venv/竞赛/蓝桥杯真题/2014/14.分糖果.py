# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/3/9 15:15'

# 模拟算法过程
n = int(input())
dp1 = list(map(int, input().strip().split())) # 每人持有的糖果数量
dp2 = [0 for _ in range(n)]  # 存储各人减少的量用来给下一个轮回加上
count = 0
while len(set(dp1)) > 1:
    for i in range(n):
        dp1[i] /= 2
        if i:
            dp2[i - 1] = dp1[i]
        else:
            dp2[n - 1] = dp1[i]
    for j in range(n):
        dp1[j] += dp2[j]
        if dp1[j] % 2 == 1:
            dp1[j] += 1
            count += 1

print(count)
