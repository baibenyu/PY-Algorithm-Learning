# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/3/18 9:38'

import time
import math

start = time.clock()
dp = [0 for _ in range(10001)]
n = int(input())
choice = []
for i in range(n):
    temp = int(input())
    choice.append(temp)
    dp[temp] = 1
    if i == 0:
        g = temp
    else:
        g = math.gcd(g, temp)

choice.sort()
dp[0] = 1
# 本题考查了数学：拓展欧几里得以及DP完全背包问题
# 拓展欧几里得：
# 设方程ax+by=C，C是gcd(a,b)的倍数
# 若a,b互质，则方程一定有解且解的数无穷
# 若不互质，则有无限多个C导致方程无解
# 例如：
# 如果gcd(a,b)==1,则仅有部分C凑不出，且能找到凑不出的C的最大值，最大值为：a*b-a-b(公式)
# 如果gcd(a,b)!=1，比如等于k,那么我们只能凑出k的整数倍
# 所以肯定有INF个数字不是K的倍数
if g != 1:
    print("INF")
else:
    for j in range(10001):
        for x in range(len(choice)):
            if j >= choice[x]:
                dp[j] = dp[j] or dp[j - choice[x]]
            else:
                break
print(10001 - sum(dp))
end = time.clock()
print(end - start)

