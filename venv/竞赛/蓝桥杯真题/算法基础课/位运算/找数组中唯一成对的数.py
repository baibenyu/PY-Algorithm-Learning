# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/3/14 19:37'

import time

start = time.clock()
# 位运算,利用异或的特性
nums = list(map(int, input().strip().split()))
ans = 0
for j in range(len(nums)):
    ans ^= j ^ nums[j]
print(ans)
# 暴力,统计数组中各数的个数
end = time.clock()
print(end - start)
