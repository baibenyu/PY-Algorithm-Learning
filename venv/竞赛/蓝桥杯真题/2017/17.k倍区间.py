# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/3/17 21:47'

import time

start = time.clock()

n, k = map(int, input().strip().split())
modk = [0 for i in range(k)]
prefix = 0  # 前缀和
count = 0
for i in range(n):
    temp = int(input().strip())
    prefix += temp
    modk[prefix % k] += 1  # 统计前缀和modk结果相同的区间数,即同类非k倍区间,同类是为了消除n的影响
for j in range(k):
    count += modk[j] * (modk[j] - 1) // 2  # 等差数列求和公式,或者C(n,2)组合
count += modk[0]  # 本身就是k倍区间无需组合
print(count)

end = time.clock()
print(end - start)
