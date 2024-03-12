# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/3/14 19:44'

import time

start = time.clock()
# 异或特点,消除相同的数,剩下的就是只有一个的数
nums = list(map(int, input().strip().split()))
ans = 0
for j in range(len(nums)):
    ans ^= nums[j]
print(ans)
end = time.clock()
print(end - start)
