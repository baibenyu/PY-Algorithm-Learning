# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/3/9 15:34'

# 博弈问题,将和尚要走的台阶转为石子数,将两个和尚构成的环境视为一个堆
k = list(map(int, input().strip().split()))
kl = len(k)
b = [0 for _ in range(kl - 1)]  # 堆的数量是和尚数-1

for i in range(1, kl):  # 放堆
    b[i - 1] = k[i] - k[i - 1] - 1
sum_up = 0

for i in range(0, kl - 1, 2):  # 进行异或，每两个和尚组成一堆. 每两堆为一组,组与组之间的台阶数不纳入考虑,因为一个人任意移动,另一个人均可以通过做出相同的操作来抵消影响
    sum_up ^= b[i]
if sum_up == 0:  # 若开始局面为0 则必输
    print(-1)
else:  # 若非0 则必赢，因此 需要找到第一步 将局面变为0 的步骤

    for i in range(kl - 1):  # 枚举移动第i堆  使得剩下的局面异或等于0，
        j = 1
        while True:  # 枚举可以移动的步数  保证 前项移动j 步后 不会超过后项
            # print(k)
            if k[i] + j >= k[i + 1]:
                break
            b[i] -= j  # 拿走 j个 ，这里代表 前一个向上移动j步
            if i != 0:
                b[i - 1] += j  # 它的后一堆b[i]向取走了j个，那莫前一堆 b[i-1] 则要增加j个 第一堆除外
            sum_up = 0
            for s in range(0, kl - 1, 2):  # 进行异或,重新计算局面
                sum_up ^= b[s]
            if sum_up == 0:
                print(k[i], k[i] + j)  # 若变成0  则后手必败，先手必赢。跳出即可；
                break
            b[i] += j  # 回溯 这不是必赢的操作
            if i != 0:
                b[i - 1] -= j
            j += 1
