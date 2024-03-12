# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/3/17 19:26'

import time

start = time.clock()
# 仅适用于无重复数组
nums = list(map(int, input().strip().split()))
begin, end = 0, len(nums) - 1
if nums[begin] < nums[end]:  # 无旋转情况
    print(nums[begin])

while begin < end - 1:  # 最小值总在无序的一边
    mid = (begin + end) // 2
    if nums[mid] >= nums[begin]:
        begin = mid
    else:
        end = mid
print(nums[end])

end = time.clock()
print(end - start)
